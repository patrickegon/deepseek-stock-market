import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Configurações ============================================================
tickers = ["AAPL", "GOOG", "MSFT", "NVDA", "BIDU", "META", "ORCL", "AMD", "AVGO", "MU"]
data_inicio = "2020-01-01"
data_fim = "2025-04-02"  # Atualize para a data atual se necessário
data_lancamento = "2025-01-20"
data_lancamento_dt = pd.to_datetime(data_lancamento)  # Convertido aqui para uso global

# 2. Download e Processamento =================================================
def baixar_dados(tickers, inicio, fim):
    try:
        return yf.download(
            tickers,
            start=inicio,
            end=fim,
            group_by='ticker',
            progress=False
        )
    except Exception as e:
        print(f"Erro no download: {e}")
        return pd.DataFrame()

dados_acoes = baixar_dados(tickers, data_inicio, data_fim)

# Construção do DataFrame consolidado
df_consolidado = pd.DataFrame()
if not dados_acoes.empty:
    for ticker in tickers:
        if ticker in dados_acoes.columns.get_level_values(0):
            df_ticker = dados_acoes[ticker][['Close']].copy()
            df_ticker.columns = [f'{ticker}_Close']
            df_ticker[f'{ticker}_Pct_Change'] = df_ticker[f'{ticker}_Close'].pct_change()
            df_consolidado = pd.concat([df_consolidado, df_ticker], axis=1)

# 3. Análise de Volatilidade ==================================================
if not df_consolidado.empty:
    # Cálculo da volatilidade
    janela_volatilidade = 20
    for ticker in tickers:
        col_pct = f'{ticker}_Pct_Change'
        if col_pct in df_consolidado.columns:
            df_consolidado[f'{ticker}_Volatilidade'] = (
                df_consolidado[col_pct].rolling(janela_volatilidade).std()
            )

    # Comparação pré/pós-evento
    mask_pre = df_consolidado.index < data_lancamento_dt
    mask_pos = df_consolidado.index >= data_lancamento_dt
    
    vol_antes = df_consolidado[mask_pre].filter(like='_Volatilidade').mean()
    vol_depois = df_consolidado[mask_pos].filter(like='_Volatilidade').mean()

    print("\nVolatilidade Média Pré-Evento (20 dias):")
    print(vol_antes)
    print("\nVolatilidade Média Pós-Evento (20 dias):")
    print(vol_depois)

    # 4. Análise de Impacto do Evento =========================================
    dias_antes = 30
    dias_depois = 30
    
    df_consolidado['Dias_Desde_Evento'] = (df_consolidado.index - data_lancamento_dt).days
    estudo_evento = df_consolidado[
        (df_consolidado['Dias_Desde_Evento'] >= -dias_antes) & 
        (df_consolidado['Dias_Desde_Evento'] <= dias_depois)
    ].copy()

    # Cálculo retornos cumulativos
    for ticker in tickers:
        col_pct = f'{ticker}_Pct_Change'
        if col_pct in estudo_evento.columns:
            estudo_evento[f'{ticker}_Retorno_Cumulativo'] = (1 + estudo_evento[col_pct]).cumprod() - 1

    # 5. Visualizações Integradas ==============================================
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 1)
    
    # Gráfico 1: Preços
    ax1 = fig.add_subplot(gs[0])
    for ticker in tickers:
        col = f'{ticker}_Close'
        if col in df_consolidado.columns:
            ax1.plot(df_consolidado[col], label=ticker, alpha=0.7)
    ax1.axvline(data_lancamento_dt, color='red', linestyle='--')
    ax1.set_title('Evolução dos Preços')
    ax1.legend(bbox_to_anchor=(1.02, 1))
    
    # Gráfico 2: Retorno Cumulativo
    ax2 = fig.add_subplot(gs[1])
    for ticker in tickers:
        col = f'{ticker}_Retorno_Cumulativo'
        if col in estudo_evento.columns:
            ax2.plot(estudo_evento['Dias_Desde_Evento'], estudo_evento[col], label=ticker)
    ax2.axvline(0, color='red', linestyle='--')
    ax2.set_title('Retorno Cumulativo (Janela de 60 Dias)')
    ax2.set_xlabel('Dias Relativos ao Evento')
    
    # Gráfico 3: Volatilidade
    ax3 = fig.add_subplot(gs[2])
    for ticker in tickers:
        col = f'{ticker}_Volatilidade'
        if col in df_consolidado.columns:
            ax3.plot(df_consolidado[col], label=ticker, alpha=0.7)
    ax3.axvline(data_lancamento_dt, color='red', linestyle='--')
    ax3.set_title('Volatilidade (Desvio Padrão de 20 Dias)')
    
    plt.tight_layout()
    plt.show()

else:
    print("Nenhum dado disponível para análise.")\n# Nova atualizaçã
