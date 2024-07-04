import matplotlib.pyplot as plt
import os

def bar_chart(labels, values,name):
    fig, axes = plt.subplots(figsize=(10,6))
    axes.bar(labels,values,color='blue')
    
    axes.set_title(f'Análisis de riesgo {name} ')
    axes.set_xlabel('Tipo de suceso')
    axes.set_ylabel('N° de sucesos')
    axes.set_xticklabels(labels, rotation=45, ha='right', fontsize='medium', wrap=True)
    
    plt.tight_layout()
    plt.savefig(f'imgs/risk_{name}.png')
    plt.close()
    
    return 'Grafico creado!'
    
if __name__ == '__main__':
  bar_chart(labels,values)