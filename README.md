Proyecto Automatización de API Urban Grocers 

Proyecto de bootcamp para automatizar pruebas basadas en la lista de comprobacion descrita en este archivo
para la API Urban Grocers que es un stock para pedir comida por medio de kits que solicita el usuario.
A groso modo lo que se hace es enviar una solicitud POST para crear un usuario nuevo y posteriormente se realiza
otra solicitud POST para nombrar y crear un nuevo kit con las restricciones descritas a continuación:

| № | Caso de Prueba | Input (JSON) | Resultado Esperado (ER) |
| :-- | :--- | :--- | :--- |
| **01** | Límite mínimo (1 carácter) | `{"name": "a"}` | **201** - Éxito: "name" coincide con la solicitud. |
| **02** | Límite máximo (511 carácteres) | `{"name": "A...[511 chars]"}` | **201** - Éxito: "name" coincide con la solicitud. |
| **03** | Campo vacío (0 carácteres) | `{"name": ""}` | **400** - Bad Request. |
| **04** | Excede el límite (512 carácteres) | `{"name": "A...[512 chars]"}` | **400** - Bad Request. |
| **05** | Caracteres especiales | `{"name": "№%@,"}` | **201** - Éxito: "name" coincide. |
| **06** | Uso de espacios | `{"name": " A Aaa "}` | **201** - Éxito: "name" coincide. |
| **07** | Números en string | `{"name": "123"}` | **201** - Éxito: "name" coincide. |
| **08** | Parámetro ausente | `{ }` | **400** - Bad Request. |
| **09** | Tipo de dato incorrecto (Integer) | `{"name": 123}` | **400** - Bad Request. |

La documentación de los endpoints con los que se trabaja en este proyecto esta contenida en: https://cnt-a2a6700e-1df5-422b-ad11-e263175cffac.containerhub.tripleten-services.com/docs/

Para desarrollar este proyecto se utilizaron conceptos básicos de python como: diferentes tipos de datos, variables,
constantes, concatenación de datos, diccionarios y sus métodos y funciones de 1 y 2 parametros.
El IDE necesario para ejecutar el proyecto es PyCharm 2026.1 con su package PyTest 7.4.4.
También se utilizaron comandos básicos de Git Bash para clonar y empujar (push) el proyecto desde y hacia GitHub.

### 🎥 Video demostrativo

![](media/API_Urban_Grocers_Automation.mp4)