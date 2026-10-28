
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Desenvolva um jogo da Forca em Python no qual o jogador tenta adivinhar uma palavra oculta antes de esgotar as tentativas. A atividade pratica listas, strings, seleção aleatória, loops, condicionais e entrada de dados.

## 📝 Tarefas

### 🛠️ Preparar a Partida

#### Descrição
Escolha uma palavra aleatoriamente da lista disponível e inicialize as variáveis que serão usadas para acompanhar o estado do jogo.

#### Requisitos
O programa concluído deve:

- Selecionar a palavra secreta aleatoriamente da lista predefinida usando o módulo `random`.
- Inicializar uma coleção vazia para registrar as letras já adivinhadas.
- Definir o limite de tentativas incorretas e iniciar o contador de erros em zero.

### 🛠️ Implementar as Rodadas

#### Descrição
Crie o loop principal para receber palpites e atualizar o progresso enquanto a partida ainda estiver em andamento.

#### Requisitos
O programa concluído deve:

- Mostrar a palavra como letras adivinhadas e espaços em branco para as letras restantes, por exemplo, `_ _ _`.
- Solicitar ao jogador uma letra por rodada e verificar se ela pertence à palavra secreta.
- Registrar letras corretas e aumentar o contador de erros quando o palpite estiver incorreto.
- Mostrar quantas tentativas incorretas ainda restam.

### 🛠️ Encerrar a Partida

#### Descrição
Defina as condições de vitória e derrota e encerre o loop quando uma delas for alcançada.

#### Requisitos
O programa concluído deve:

- Encerrar com vitória quando todas as letras da palavra forem adivinhadas.
- Encerrar com derrota quando o limite de tentativas incorretas for atingido.
- Exibir uma mensagem indicando o resultado e revelar a palavra secreta em caso de derrota.