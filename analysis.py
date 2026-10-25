"""Retail sales descriptive analysis using a synthetic example dataset."""
import argparse,json
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
COLUMNS=['order_id','order_date','category','product','quantity','unit_price_pkr']
def analyze(path,out):
    df=pd.read_csv(path)
    missing=set(COLUMNS)-set(df.columns)
    if missing:raise ValueError(f'Missing columns: {sorted(missing)}')
    if df.empty or df[COLUMNS].isna().any().any():raise ValueError('Empty dataset or missing values')
    if df.order_id.duplicated().any():raise ValueError('Duplicate order IDs')
    df['order_date']=pd.to_datetime(df['order_date'],errors='raise')
    for col in ['quantity','unit_price_pkr']:
        df[col]=pd.to_numeric(df[col],errors='raise')
        if not (df[col]>0).all():raise ValueError(f'{col} must be positive')
    df['revenue_pkr']=df.quantity*df.unit_price_pkr
    df['month']=df.order_date.dt.to_period('M').astype(str)
    monthly=df.groupby('month',as_index=False).agg(revenue_pkr=('revenue_pkr','sum'),orders=('order_id','count'))
    categories=df.groupby('category',as_index=False).agg(revenue_pkr=('revenue_pkr','sum'),units=('quantity','sum')).sort_values('revenue_pkr',ascending=False)
    products=df.groupby('product',as_index=False).agg(units=('quantity','sum'),revenue_pkr=('revenue_pkr','sum')).sort_values('units',ascending=False)
    summary={'orders':int(len(df)),'total_revenue_pkr':int(df.revenue_pkr.sum()),'units_sold':int(df.quantity.sum()),'average_order_value_pkr':round(float(df.revenue_pkr.mean()),2),'top_category_by_revenue':str(categories.iloc[0].category),'top_product_by_units':str(products.iloc[0]['product'])}
    out.mkdir(parents=True,exist_ok=True)
    monthly.to_csv(out/'monthly_summary.csv',index=False);categories.to_csv(out/'category_summary.csv',index=False);products.to_csv(out/'product_summary.csv',index=False)
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    fig,ax=plt.subplots(figsize=(9,5));ax.plot(monthly.month,monthly.revenue_pkr,marker='o');ax.set(title='Monthly Revenue (Synthetic Retail Data)',xlabel='Month',ylabel='Revenue (PKR)');ax.tick_params(axis='x',rotation=45);fig.tight_layout();fig.savefig(out/'monthly_revenue.png',dpi=160);plt.close(fig)
    fig,ax=plt.subplots(figsize=(8,5));ax.bar(categories.category,categories.revenue_pkr);ax.set(title='Revenue by Category',ylabel='Revenue (PKR)');fig.tight_layout();fig.savefig(out/'category_revenue.png',dpi=160);plt.close(fig)
    fig,ax=plt.subplots(figsize=(8,5));top=products.head(8);ax.barh(top['product'][::-1],top.units[::-1]);ax.set(title='Top Products by Units Sold',xlabel='Units sold');fig.tight_layout();fig.savefig(out/'top_products.png',dpi=160);plt.close(fig)
    return summary
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,default=Path('data/retail_sales.csv'));p.add_argument('--out',type=Path,default=Path('outputs'));a=p.parse_args();print(json.dumps(analyze(a.data,a.out),indent=2))
