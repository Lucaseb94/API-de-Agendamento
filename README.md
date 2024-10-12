# Sistema de Agendamento

Este projeto é uma API de agendamento, que permite gerenciar agendamentos para prestadores de serviços. Ele foi desenvolvido usando Django e Django Rest Framework, e inclui permissões personalizadas para garantir que apenas usuários autorizados possam visualizar ou modificar os dados.

## Funcionalidades

- **Listagem e Criação de Agendamentos**: 
  - Prestadores podem visualizar seus agendamentos.
  - Usuários autorizados podem criar novos agendamentos.
  
- **Atualização e Exclusão de Agendamentos**:
  - Apenas o prestador que criou o agendamento pode atualizá-lo ou excluí-lo.
  
- **Listagem de Prestadores**: 
  - Apenas superusuários podem visualizar a lista de prestadores cadastrados.
  
- **Verificação de Horários Disponíveis**:
  - A API oferece um endpoint para verificar os horários disponíveis de agendamento para uma data específica.

## Tecnologias Utilizadas

- **Django** - Framework web usado para o backend.
- **Django Rest Framework** - Extensão para facilitar a construção de APIs com Django.
- **Python** - Linguagem de programação usada no projeto.

## Endpoints Principais

### Agendamentos

- **Listar e criar agendamentos**:  
  `GET` e `POST` em `/agendamentos/`  
  Parâmetro opcional: `username` (para filtrar os agendamentos de um prestador).

- **Detalhar, atualizar e excluir agendamento**:  
  `GET`, `PUT`, `DELETE` em `/agendamentos/<id>/`

### Prestadores

- **Listar prestadores** (somente para superusuários):  
  `GET` em `/prestadores/`

### Horários Disponíveis

- **Obter horários disponíveis para uma data específica**:  
  `GET` em `/horarios/?data=<YYYY-MM-DD>`  
  Exemplo: `/horarios/?data=2024-10-10`

  Se a data não for passada, será usado o dia atual.

## Permissões

As permissões do projeto foram configuradas para garantir segurança no acesso aos dados:

- **IsOwnerOrCreateOnly**: Permite que o usuário crie agendamentos, mas apenas visualize seus próprios agendamentos.
- **IsPrestador**: Apenas o prestador que criou o agendamento pode modificá-lo ou excluí-lo.
- **Isadm**: Apenas superusuários podem acessar a lista de prestadores.
- **IsSuperUser**: Similar a `Isadm`, garantindo que apenas superusuários acessem áreas restritas.
