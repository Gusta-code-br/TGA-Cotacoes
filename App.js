import React, { useState, useEffect } from 'react';
import './App.css'; // Importe o arquivo CSS aqui

const FormularioProdutos = () => {
    const [codprd, setProdutos] = useState([]);
    const [formData, setFormData] = useState({});
    const [responseMessage, setResponseMessage] = useState('');

    useEffect(() => {
        fetch('http://localhost/API-TGA/create-form-api.php')
            .then(response => response.json())
            .then(data => setProdutos(data));
    }, []);

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const newData = [];
        Object.keys(formData).forEach((key) => {
            const nseq = key; // Obtém o ID do produto selecionado
            const valor = parseFloat(formData[key]); // Obtém o valor do input como um número
            if (!isNaN(valor)) {
                newData.push({ nseq: nseq, valor: valor });
            } else {
                console.error(`Valor inválido para o produto ${nseq}`);
            }
        });
    
        fetch('http://localhost/API-TGA/update-value-api.php', {
            method: 'POST',
            body: JSON.stringify(newData),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => setResponseMessage(data.message))
        .catch(error => console.error('Erro:', error));
    };
    
    return (
        <div>
            <header>
                <h1>TGA-Cotação</h1>
            </header>
            <form onSubmit={handleSubmit}>
                {codprd.map(codprd => (
                    <div class="item" key={codprd.nseq} style={{ display: 'flex', marginBottom: '10px' }}>
                        <label style={{ flex: '1', marginRight: '10px' }}>{codprd.nseq}: {codprd.nomefantasia}</label>
                        <input
                            type="text"
                            name={codprd.nseq}
                            onChange={handleChange}
                        />
                    </div>
                ))}
                <button type="submit">Enviar</button>
            </form>
            {responseMessage && <p>{responseMessage}</p>}
        </div>
    );
};

export default FormularioProdutos;
