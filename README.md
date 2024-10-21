# Mapeamento do Processo

[Versão em Português](#portuguese) | [Version in English](#english)

## Mapeamento do Processo:

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
       Aperte **Ctrl + L**.  
       Componente = Part Number (PN) do material encontrado na página do workon.  
       Quantidade = **1**.  
       Aperte **Enter** e depois **Ctrl + S**.

   - **NÃO:**  
     - **Transação IB01:**  
       Cole o número de inventário com subconjunto na área "Equipamento".  
       Preencha o campo "Utilização" com o número **4 (Manutenção)**.  
       Aperte **Enter**.  
       Selecione uma linha vazia para adicionar as informações do equipamento.  
       Aperte **Ctrl + L**.  
       Componente = Part Number (PN) do material encontrado na página do workon.  
       Quantidade = **1**.  
       Aperte **Enter** e depois **Ctrl + S**.

---

## Process Mapping:

1. **Received Email**  
   Receive the workon request in the inbox.

2. **Access Workon**  
   Open workon in the browser.

3. **Copy Inventory**  
   Copy the inventory where the material will be inserted.

4. **Paste in Transaction IH03**  
   Paste it into transaction IH03 in the first field.

5. **Check Checklists**  
   Check all boxes in the checklist.

6. **Pull Inventory Data**  
   Click on the clock to pull the inventory data.

7. **Find Subset**  
   Find the specified subset in workon. If not found, use the subset **"PECA"**.

8. **Copy Inventory with Subset**  
   Copy the inventory with the subset.

9. **Is there any equipment within this subset?**
   - **YES:**  
     - **Transaction IB02:**  
       Paste the inventory number with the subset in the "Equipment" area.  
       Fill in the "Utilization" field with the number **4 (Maintenance)**.  
       Press **Enter**.  
       Select an empty row to add the equipment information.  
       Press **Ctrl + L**.  
       Component = Part Number (PN) of the material found on the workon page.  
       Quantity = **1**.  
       Press **Enter** and then **Ctrl + S**.

   - **NO:**  
     - **Transaction IB01:**  
       Paste the inventory number with the subset in the "Equipment" area.  
       Fill in the "Utilization" field with the number **4 (Maintenance)**.  
       Press **Enter**.  
       Select an empty row to add the equipment information.  
       Press **Ctrl + L**.  
       Component = Part Number (PN) of the material found on the workon page.  
       Quantity = **1**.  
       Press **Enter** and then **Ctrl + S**.
