import React, { useState } from 'react';
import axios from 'axios';

const Upload = () => {
    const [file, setFile] = useState(null);   // Para manejar el archivo cargado
    const [graphUrl, setGraphUrl] = useState(null);  // Para manejar la URL del gráfico
    const [errorMessage, setErrorMessage] = useState('');  // Para manejar mensajes de error

    // Maneja la selección de archivos
    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    // Envía el archivo al backend y obtiene el gráfico
    const handleUpload = async () => {
        if (!file) {
            setErrorMessage("Por favor, selecciona un archivo.");
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:5000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
                responseType: 'blob',  // Para recibir la imagen como blob
            });

            // Convierte la imagen recibida en una URL que se pueda mostrar en la página
            const imageUrl = URL.createObjectURL(response.data);
            setGraphUrl(imageUrl);  // Guarda la URL del gráfico para mostrarlo
            setErrorMessage('');    // Limpia cualquier mensaje de error
        } catch (error) {
            setErrorMessage("Hubo un problema al subir el archivo.");
            console.error(error);
        }
    };

    return (
        <div style={{ maxWidth: '600px', margin: 'auto', padding: '20px', fontFamily: 'Arial' }}>
            <h2 style={{ textAlign: 'center', color: '#4A90E2' }}>Sube tu archivo Excel</h2>
            
            <input type="file" onChange={handleFileChange} style={{ display: 'block', margin: '20px auto' }} />
            
            <button 
                onClick={handleUpload} 
                style={{ display: 'block', margin: '20px auto', backgroundColor: '#4A90E2', color: 'white', padding: '10px', borderRadius: '5px', cursor: 'pointer', border: 'none' }}
            >
                Probar el método con los 1000 datos
            </button>

            {errorMessage && <p style={{ color: 'red', textAlign: 'center' }}>{errorMessage}</p>}

            {graphUrl && (
                <div style={{ marginTop: '30px', textAlign: 'center' }}>
                    <h3>Gráfico generado:</h3>
                    <img src={graphUrl} alt="Gráfico generado por el backend" style={{ maxWidth: '100%' }} />
                </div>
            )}
        </div>
    );
};

export default Upload;
