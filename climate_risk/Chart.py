import matplotlib.pyplot as plt
import os

def bar_chart(labels, values,name):
    fig, ax = plt.subplots(figsize=(10, 6))  # Ajustar el tamaño de la figura según sea necesario
    
    bars = ax.bar(labels, values)
    
    # Rotar las etiquetas del eje x en 45 grados y ajustar tamaño de fuente
    ax.set_xticklabels(labels, rotation=45, ha='right', fontsize='medium', wrap=True)  # 'wrap=True' permite el ajuste automático
    
    # Ajustar tamaño de fuente automáticamente para el eje y
    ax.tick_params(axis='y', labelsize='medium')
    
    # Añadir etiquetas de valor a cada barra
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 puntos de desplazamiento vertical
                    textcoords="offset points",
                    ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig(f'imgs/Historical_risk_{name}.png')
    plt.close()
    
    return 'Grafico creado!'
    
if __name__ == '__main__':
  bar_chart(labels,values)