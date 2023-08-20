# Integração Google Calendar com Notion

O projeto de integração entre o **Google Calendar** e a plataforma **Notion** tem como objetivo proporcionar uma sincronização eficiente entre a sua agenda do Google Calendar e um banco de dados no Notion, apresentando esses eventos em uma visualização de calendário dentro do Notion. Isso permitirá que você tenha uma visão unificada de seus compromissos e tarefas, melhorando a gestão do seu tempo e aumentando a produtividade.

## Funcionalidades

- **Sincronização Bidirecional:** O projeto permite a sincronização de eventos entre o Google Calendar e o Notion, garantindo que as atualizações feitas em qualquer plataforma sejam refletidas na outra.

- **Visualização de Calendário no Notion:** A integração possibilita a exibição dos eventos do Google Calendar em uma visualização de calendário diretamente no Notion, tornando mais fácil a visualização dos seus compromissos.

- **Detalhes de Eventos:** Além da visualização de calendário, os detalhes dos eventos são integrados ao Notion. Isso inclui informações como título, data, horário e descrição.

- **Personalização Flexível:** O projeto oferece opções para personalizar a forma como os eventos são exibidos no Notion, permitindo que você escolha quais calendários do Google deseja sincronizar e como deseja que os eventos sejam formatados no Notion.

## Configuração

1. **Crie uma Conta de Desenvolvedor no Google Cloud:**
   - Acesse o [Google Cloud Console](https://console.cloud.google.com/).
   - Crie um novo projeto para a integração.
   - Ative a API do Google Calendar e crie as credenciais necessárias (chave de API ou credenciais OAuth 2.0).

2. **Obtenha as Credenciais do Notion:**
   - Dependendo da API do Notion utilizada, você precisará gerar tokens de autenticação ou chaves de API para acessar e modificar sua base de dados.

3. **Configuração do Projeto:**
   - Clone ou baixe o repositório do projeto.
   - Configure as credenciais do Google e do Notion no arquivo de configuração do projeto.

4. **Configuração da Sincronização:**
   - Defina as configurações de sincronização, como quais calendários do Google deseja sincronizar com qual base de dados do Notion.

5. **Execução:**
   - Execute o script de sincronização para iniciar o processo de integração.
   - O script deve buscar eventos no Google Calendar e atualizar a base de dados correspondente no Notion.

6. **Agendamento de Sincronização:**
   - Configure um agendador para executar o script de sincronização em intervalos regulares, garantindo que as informações permaneçam atualizadas.

# "Você enquanto desenvolvedor, porque contribuir em projetos open source? Primeiro, porque você tem um problema com o software que você usa e quer ver consertado ou você quer uma funcionalidade que a comunidade não parece interessada em fazer. A idéia toda de open source é que você coce sua própria coceira. A postura da maioria dos desenvolvedores é ser bem folgado, povo só posta “ow, e aí, quando vocês vão fazer a funcionalidade lá que eu pedi 2 meses atrás?” Folgado pra caramba. Povo que mantém os projetos tem que ser super paciente, porque se fosse eu já respondia “eu vou fazer a hora que você me pagar, folgado”. Se você é desenvolvedor e nem você que precisa da funcionalidade se deu ao trabalho de tentar implementar, porque outra pessoa vai fazer pra você de graça? Se liga, é assim que você começa com o pé esquerdo." 

## -Akita PUTASSO. Fábio.


