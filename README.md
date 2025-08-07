# 📽️ Análise de Sentimentos em Reviews de Filmes – Projeto Didático

---

## 🧠 Objetivo
Este projeto tem como finalidade estudar os principais conceitos de Processamento de Linguagem Natural (PLN) e técnicas de vetorização de texto, aplicando-os na análise de sentimentos de reviews de filmes extraídas da plataforma IMDB.
O foco está no aprendizado e experimentação, passando por modelos clássicos até redes neurais profundas e fine-tuning de modelos pré-treinados.

## 🔍 Motivação
A linguagem usada em críticas de filmes é rica e subjetiva. Com isso, este projeto visa não apenas treinar modelos para classificar reviews como positivas ou negativas, mas também entender como a linguagem expressa sentimentos, quais técnicas são mais eficazes em diferentes abordagens e como as diferentes etapas de um pipeline de PLN afetam o desempenho dos modelos.

## 🚧 Status do Projeto
Em desenvolvimento
As etapas estão sendo construídas de forma incremental com foco no aprendizado teórico-prático. A eficiência dos modelos não é o principal critério, mas sim o entendimento de cada etapa.

## Etapas do Projeto
Coleta e Pré-processamento dos Dados
- Escolha do Dataset
- Limpeza textual: remoção de ruídos, normalização, tokenização, etc.
- Redução morfológica: lematização

Análise Exploratória de Dados (EDA)
- Visualizações estatísticas
- Palavras mais frequentes em cada classe
- Verificação de desequilíbrios nos dados (palavras não legivéis)

Técnicas de vetorização:
- Bag-of-Words (BoW)
- TF-IDF
- Word Embeddings: Word2Vec, GloVe, FastText
- Embeddings Contextuais: BERT, RoBERTa, etc.

Treinamento de Modelos
- Modelos clássicos: Naive Bayes, SVM, Regressão Logística
- Redes neurais: RNNs / LSTMs / CNNs
- Transformers (via fine-tuning de BERT e derivados)

Avaliação
- Métricas: Acurácia, Precisão, Recall, F1-Score
- Análise de erros

## 🤝 Colaboração
Sinta-se à vontade para abrir issues, propor melhorias, sugerir bibliografia ou compartilhar insights sobre abordagens de PLN. Este é um projeto didático e colaborativo!