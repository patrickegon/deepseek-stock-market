[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# **Sumário:**
<!--ts-->
   * [Introdução](#intro)
   * [Contexto: 🧠 DeepSeek: A Revolução da IA Aberta](#cont)
   * [📌 Resumo Executivo](#resumo)
   * [1. 🚀 Introdução ao DeepSeek](#introd)
   * [2. ⚙️ Tecnologia e Inovações](#tec)
   * [3. 📉 Impacto no Mercado](#imp)
   * [4. 📊 Caso de Uso: FinRL-DeepSeek](#uso)
   * [5. 🌐 Ecossistema Open-Source](#eco)
   * [6. 📌 Conclusão](#conc)
   * [7. Referências](#ref)
   * [Contato](#contact)
   <!--te-->


<a name="intro"></a>
# **Introdução**

Neste projeto apliquei os conhecimentos obtidos no módulo 3 do Bootcamp de Data Science Aplicada da Alura. Todo arcabouço teórico adquirido até aqui foi aplicado para o entendimento das nuances envolvendo as séries temporais. Da estatística descritiva, passando pela análise exploratória e chegando às previsões, utilizando ferramentas específicas para esse tipo de dados, como o StatisModel e Prophet desenvolvido pelo Facebook. 

O Notebook com a análise completa e códigos pode ser encontrado [aqui](https://github.com/vqrca/bootcamp_alura_projeto_3/blob/main/Notebooks/Projeto_3_Valquiria_Alencar.ipynb). 
> Recomendo que seja aberto pelo google colab para melhorar a visualização!

<a name="resumo"></a>
## **Contexto: 🧠 DeepSeek: A Revolução da IA Aberta**

DeepSeek é uma startup chinesa de IA fundada em julho de 2023 em Hangzhou, que lançou modelos de grande escala com custo e consumo de energia drasticamente inferiores aos concorrentes, abalando o mercado global. 
Seu modelo inicial, DeepSeek-R1, foi elogiado por líderes do setor, mas desencadeou a maior queda diária de capitalização da Nvidia em US$ 593 bilhões em janeiro de 2025. 
Em seguida, o DeepSeek-V3 (671 B parâmetros) incorporou arquitetura mixture-of-experts e balanceamento avançado de carga, provando eficiência comparável a modelos como GPT-4, ao custo de apenas US$ 6 milhões de treinamento e consumindo 10 % da energia de rivais.

*[[1]] Wikipédia - Hangzhou DeepSeek AI(https://en.wikipedia.org/wiki/DeepSeek).*

*[[2]] pbs.org(https://------------------).*



<a name="cont"></a>
## **📌 Resumo Executivo:**

Fundação & Missão: Hangzhou DeepSeek Artificial Intelligence Basic Technology Research Co., Ltd. foi criada em 17 de julho de 2023 por Liang Wenfeng, com o objetivo de democratizar IA via modelos open-weight de baixo custo
*Fonte: Wikipedia [[3]](https://en.wikipedia.org/wiki/DeepSeek).*


DeepSeek-R1: Lançado em janeiro de 2025, oferece desempenho próximo ao GPT-4 por uma fração do custo computacional.


DeepSeek-V3: Com 671 bilhões de parâmetros, ativa apenas 37 B por token, reduzindo o custo de inferência e incorporando Multi-head Latent Attention para balanceamento robusto
*Fonte: Wikipedia [[3]](https://en.wikipedia.org/wiki/DeepSeek).*


<a name="introd"></a>
## **1. 🚀 Introdução ao DeepSeek**

Fundação: Julho de 2023, Hangzhou, China, por Liang Wenfeng
*Fonte: Wikipedia [[3]](https://en.wikipedia.org/wiki/DeepSeek).*

DeepSeek-R1: Lançado jan/2025, “um presente para a indústria global de IA”, segundo Jensen Huang, CEO da Nvidia
El País

Open-Weight: Parâmetros liberados publicamente, fortalecendo a comunidade de pesquisa.

<a name="tec"></a>
### **2. ⚙️ Tecnologia e Inovações**
### **2.1 Arquitetura Mixture-of-Experts (MoE)**


V3: 671 B parâmetros, 37 B ativados por token, via MoE, reduzindo drasticamente uso de GPU
*Fonte: Wikipedia [[3]](https://en.wikipedia.org/wiki/DeepSeek).*

MLA: Multi-head Latent Attention para eficiência e balanceamento sem perda auxiliar.



### **2.2 Treinamento & Sustentabilidade**

Custo: US $ 6 mi para treinar V3 vs. US $ 100 mi do GPT-4
*Fonte: Wikipedia [[3]](https://en.wikipedia.org/wiki/DeepSeek).*

Energia: Consome 10 % da energia de modelos equivalentes.

Margem: Estimada em 545 % (US $ 87 072/dia de custo vs. US $ 562 027/dia de receita)
Time

<a name="imp"></a>
## **3. 📉 Impacto no Mercado**
### **3.1 Queda da Nvidia**

DeepSeek-R1 provocou perda de até US$ 593 bi em valor de mercado da Nvidia em um dia
Financial Times

Recuperação: +43 % no ano seguinte, refletindo confiança dos investidores
El País

### **3.2 Reações da Indústria**

Debate de Custos: Demis Hassabis questionou publicamente o custo de treinamento do DeepSeek, gerando discussões sobre transparência
theaustralian.com.au

<a name="uso"></a>
## **4. 📊 Caso de Uso: FinRL-DeepSeek**

Objetivo: Combinar DeepSeek-V3 com deep reinforcement learning para trading no Nasdaq-100.

Resultados: Superior aos benchmarks em Information Ratio e CVaR (2019–2023)
pbs.org

Repositório: https://github.com/benstaf/FinRL_DeepSeek
pbs.org

<a name="eco"></a>
## **5. 🌐 Ecossistema Open-Source**

Projeto	Repositório GitHub
DeepSeek-V3 (MoE + MLA)	https://github.com/deepseek-ai/DeepSeek-V3
*Fonte: Wikipedia [[3]](https://en.wikipedia.org/wiki/DeepSeek).*
Sistema de Arquivos 3FS	https://github.com/deepseek-ai/3FS
*Fonte: Wikipedia [[3]](https://en.wikipedia.org/wiki/DeepSeek).*
Integrações & Ferramentas	https://github.com/Zodoge/Awesome-DeepSeek-Integration
*Fonte: Wikipedia [[3]](https://en.wikipedia.org/wiki/DeepSeek).*

<a name="conc"></a>
## **6. 📌 Conclusão**

O caso DeepSeek prova que IA de alto desempenho pode ser aberta e acessível, gerando disrupção tecnológica e financeira. 
Ao estruturar este repositório de forma clara e envolvente, facilitamos o entendimento e a reprodução dos métodos que transformaram o cenário global de IA.

<a name="ref"></a>
## **📚 Referências**

[[1]] Hangzhou DeepSeek AI – Wikipédia. Available at: https://en.wikipedia.org/wiki/DeepSeek - Wikipedia

[[2]] “DeepSeek: The Quiet Giant Leading China's AI Race” – The Economist, Jan 2025.

[[3]] “How Chinese A.I. Start-Up DeepSeek Is Competing With Silicon Valley Giants” – The New York Times, Jan 2025.

[[4]] “Nvidia shares plummet as Chinese open-source AI shocks market” – The Guardian, Jan 2025. - El País

[[5]] “A startup just wiped $593 billion off Nvidia's value — here’s how” – Business Insider, Jan 2025.

[[6]] “China’s cheap, open AI model DeepSeek thrills scientists” – Nature, Jan 23 2025.

[[7]] “DeepSeek’s insane margin: US$87K/day in cost, US$562K/day in revenue” – Time, Mar 2025. - Time

[[8]] “DeepSeek’s success will undermine the US-China tech war” – Financial Times, Feb 2025. - Financial Times

[[9]] “DeepSeek focuses on research over revenue in contrast to Silicon Valley” – Financial Times, Mar 2025.

[[10]] DeepSeek-V3 Paper & GitHub: https://github.com/deepseek-ai/DeepSeek-V3 - Wikipedia

<a name="contact"></a>
## **Contato**
# **Onde encontrar meu trabalho?**
  
[Medium](-------------)
	
[LinkedIn](-----------)
 
[ResearchGate](-------------)
 
[Currículo lattes](--------)
