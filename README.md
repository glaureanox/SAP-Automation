<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mapeamento do Processo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            color: #333;
        }

        h2 {
            color: #2C3E50;
        }

        .process-step {
            margin-bottom: 20px;
            padding: 15px;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
            background-color: #ECF0F1;
        }

        .decision {
            margin: 15px 0;
            padding: 10px;
            border: 1px dashed #3498DB;
            border-radius: 5px;
            background-color: #D5E8F3;
        }

        .step-title {
            font-weight: bold;
            color: #2980B9;
        }

        .sub-step {
            margin-left: 20px;
            color: #34495E;
        }

        .highlight {
            background-color: #F9E79F;
            font-weight: bold;
            padding: 2px 5px;
            border-radius: 3px;
        }

        .language-links {
            margin-bottom: 20px;
        }

        .language-links a {
            margin-right: 15px;
            text-decoration: none;
            color: #2980B9;
            font-weight: bold;
        }

        .language-links a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<div class="language-links">
    <a href="#portuguese">Versão em Português</a>
    <a href="#english">Version in English</a>
</div>

<h2 id="portuguese"><b>Mapeamento do Processo:</b></h2>

<div class="process-step">
    <div class="step-title">1. E-mail Recebido</div>
    <p>Receber o pedido de workon na caixa de entrada.</p>
</div>

<div class="process-step">
    <div class="step-title">2. Acesso ao Workon</div>
    <p>Abrir o workon no navegador.</p>
</div>

<div class="process-step">
    <div class="step-title">3. Copiar Inventário</div>
    <p>Copiar o(s) inventário(s) onde o material será inserido.</p>
</div>

<div class="process-step">
    <div class="step-title">4. Colar na Transação IH03</div>
    <p>Cole na transação IH03 no primeiro campo.</p>
</div>

<div class="process-step">
    <div class="step-title">5. Marcar Checklists</div>
    <p>Marcar todas as caixas da checklist.</p>
</div>

<div class="process-step">
    <div class="step-title">6. Puxar Dados do Inventário</div>
    <p>Clicar no relógio para puxar os dados do inventário.</p>
</div>

<div class="process-step">
    <div class="step-title">7. Encontrar Subconjunto</div>
    <p>Encontrar o subconjunto especificado no workon. Caso não encontre, usar o subconjunto <span class="highlight">"PECA"</span>.</p>
</div>

<div class="process-step">
    <div class="step-title">8. Copiar Inventário com Subconjunto</div>
    <p>Copiar inventário com o subconjunto.</p>
</div>

<div class="decision">
    <div class="step-title">9. Existe algum equipamento dentro desse subconjunto?</div>
    <p><strong>SIM:</strong></p>
    <div class="sub-step">
        <p>Transação IB02:</p>
        <p>Cole o número de inventário com subconjunto na área "Equipamento".</p>
        <p>Preencha o campo "Utilização" com o número <span class="highlight">4 (Manutenção)</span>.</p>
        <p>Aperte <strong>Enter</strong>.</p>
        <p>Selecione uma linha vazia para adicionar as informações do equipamento.</p>
        <p>Aperte <strong>Ctrl + L</strong>.</p>
        <p>Componente = Part Number (PN) do material encontrado na página do workon.</p>
        <p>Quantidade = <span class="highlight">1</span>.</p>
        <p>Aperte <strong>Enter</strong> e depois <strong>Ctrl + S</strong>.</p>
    </div>
    
    <p><strong>NÃO:</strong></p>
    <div class="sub-step">
        <p>Transação IB01:</p>
        <p>Cole o número de inventário com subconjunto na área "Equipamento".</p>
        <p>Preencha o campo "Utilização" com o número <span class="highlight">4 (Manutenção)</span>.</p>
        <p>Aperte <strong>Enter</strong>.</p>
        <p>Selecione uma linha vazia para adicionar as informações do equipamento.</p>
        <p>Aperte <strong>Ctrl + L</strong>.</p>
        <p>Componente = Part Number (PN) do material encontrado na página do workon.</p>
        <p>Quantidade = <span class="highlight">1</span>.</p>
        <p>Aperte <strong>Enter</strong> e depois <strong>Ctrl + S</strong>.</p>
    </div>
</div>

<h2 id="english"><b>Process Mapping:</b></h2>

<div class="process-step">
    <div class="step-title">1. Received Email</div>
    <p>Receive the workon request in the inbox.</p>
</div>

<div class="process-step">
    <div class="step-title">2. Access Workon</div>
    <p>Open workon in the browser.</p>
</div>

<div class="process-step">
    <div class="step-title">3. Copy Inventory</div>
    <p>Copy the inventory where the material will be inserted.</p>
</div>

<div class="process-step">
    <div class="step-title">4. Paste in Transaction IH03</div>
    <p>Paste it into transaction IH03 in the first field.</p>
</div>

<div class="process-step">
    <div class="step-title">5. Check Checklists</div>
    <p>Check all boxes in the checklist.</p>
</div>

<div class="process-step">
    <div class="step-title">6. Pull Inventory Data</div>
    <p>Click on the clock to pull the inventory data.</p>
</div>

<div class="process-step">
    <div class="step-title">7. Find Subset</div>
    <p>Find the specified subset in workon. If not found, use the subset <span class="highlight">"PECA"</span>.</p>
</div>

<div class="process-step">
    <div class="step-title">8. Copy Inventory with Subset</div>
    <p>Copy the inventory with the subset.</p>
</div>

<div class="decision">
    <div class="step-title">9. Is there any equipment within this subset?</div>
    <p><strong>YES:</strong></p>
    <div class="sub-step">
        <p>Transaction IB02:</p>
        <p>Paste the inventory number with the subset in the "Equipment" area.</p>
        <p>Fill in the "Utilization" field with the number <span class="highlight">4 (Maintenance)</span>.</p>
        <p>Press <strong>Enter</strong>.</p>
        <p>Select an empty row to add the equipment information.</p>
        <p>Press <strong>Ctrl + L</strong>.</p>
        <p>Component = Part Number (PN) of the material found on the workon page.</p>
        <p>Quantity = <span class="highlight">1</span>.</p>
        <p>Press <strong>Enter</strong> and then <strong>Ctrl + S</strong>.</p>
    </div>
    
    <p><strong>NO:</strong></p>
    <div class="sub-step">
        <p>Transaction IB01:</p>
        <p>Paste the inventory number with the subset in the "Equipment" area.</p>
        <p>Fill in the "Utilization" field with the number <span class="highlight">4 (Maintenance)</span>.</p>
        <p>Press <strong>Enter</strong>.</p>
        <p>Select an empty row to add the equipment information.</p>
        <p>Press <strong>Ctrl + L</strong>.</p>
        <p>Component = Part Number (PN) of the material found on the workon page.</p>
        <p>Quantity = <span class="highlight">1</span>.</p>
        <p>Press <strong>Enter</strong> and then <strong>Ctrl +
