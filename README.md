# Mapeamento do Processo

---

## Versão em Português

1. **E-mail Recebido**  
   Receber o pedido de workon na caixa de entrada.

2. **Acesso ao Workon**  
   Abrir o workon no navegador.

3. **Copiar Inventário**  
   Copiar o(s) inventário(s) onde o material será inserido.

4. **Colar na Transação IH03**  
   Cole na transação IH03 no primeiro campo.

5. **Marcar Checklists**  
   Marcar todas as caixas da checklist.

6. **Puxar Dados do Inventário**  
   Clicar no relógio para puxar os dados do inventário.

7. **Encontrar Subconjunto**  
   Encontrar o subconjunto especificado no workon. Caso não encontre, usar o subconjunto **"PECA"**.

8. **Copiar Inventário com Subconjunto**  
   Copiar inventário com o subconjunto.

9. **Existe algum equipamento dentro desse subconjunto?**
   - **SIM:**  
     - **Transação IB02:**  
       Cole o número de inventário com subconjunto na área "Equipamento".  
       Preencha o campo "Utilização" com o número **4 (Manutenção)**.  
       Aperte **Enter**.  
       Selecione uma linha vazia para adicionar as informações do equipamento.  
       Preencha o campo "Ctl" com a letra **L**.  
       Componente = Part Number (PN) do material encontrado na página do workon.  
       Quantidade = **1**.  
       Aperte **Enter** e depois **Ctrl + S**.

   - **NÃO:**  
     - **Transação IB01:**  
       Cole o número de inventário com subconjunto na área "Equipamento".  
       Preencha o campo "Utilização" com o número **4 (Manutenção)**.  
       Aperte **Enter**.  
       Selecione uma linha vazia para adicionar as informações do equipamento.  
       Preencha o campo "Ctl" com a letra **L**.  
       Componente = Part Number (PN) do material encontrado na página do workon.  
       Quantidade = **1**.  
       Aperte **Enter** e depois **Ctrl + S**.

---
