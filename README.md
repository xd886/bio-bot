# EcoBot 🌱

EcoBot es un bot de Discord diseñado para promover la conciencia ecológica. Ofrece consejos diarios sobre sostenibilidad y permite consultar el tiempo de descomposición de objetos domésticos.

## Características

- **Consejos ecológicos**: Obtén un consejo aleatorio sobre cómo cuidar el medio ambiente con el comando `?biohelp`.
- **Información sobre descomposición**: Consulta cuánto tiempo tarda en descomponerse un objeto doméstico con el comando `?descomposicion <objeto>`.

## Comandos

### `?biohelp`
Proporciona un consejo ecológico aleatorio.

**Ejemplo:**

?biohelp
Respuesta:

🌱 Consejo ecológico: Usa menos plástico: lleva tu propia bolsa reutilizable cuando hagas compras.

?descomposicion <objeto>
Muestra el tiempo aproximado de descomposición de un objeto.

Ejemplo:

?descomposicion botella de plástico
Respuesta:



🕒 El tiempo de descomposición de **botella de plástico** es aproximadamente: 450 años.
Si el objeto no está en la base de datos, responderá:

❌ Lo siento, no tengo información sobre el tiempo de descomposición de **<objeto>**.
Requisitos
Python 3.8 o superior.
Librería discord.py instalada:


pip install discord.py
Token de bot de Discord.
Instalación
Clona este repositorio:



git clone https://github.com/xd886/bio-bot/tree/main
cd ecobot
Instala las dependencias necesarias:


Copiar código
pip install -r requirements.txt
Configura tu token en el archivo del bot: Reemplaza TU_TOKEN_AQUI con tu token de Discord en el código.

Ejecuta el bot:



python ecobot.py
dwww
Personalización

Consejos ecológicos: Puedes añadir más consejos a la lista eco_tips en el código.

Tiempos de descomposición: Amplía el diccionario decomposition_times con más objetos y sus tiempos de descomposición.

Ejemplo de uso

Escribe ?biohelp en tu canal de Discord para obtener un consejo ecológico.

Consulta el tiempo de descomposición de un objeto escribiendo ?descomposicion <objeto>.

Contribuciones

¡Contribuciones son bienvenidas! Si tienes ideas para mejorar EcoBot, no dudes en abrir un issue o enviar un pull request.

Licencia
Este proyecto está licenciado bajo la MIT License.

Autor
Desarrollado por Elihud Fuentes.
