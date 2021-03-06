# ValueSelectorWidget 
## Breve descripción del componente: 
Se trata de un componente personalizado desarrollado con PySide6, el cual nos permite ir alternando entre los valores del texto 
que se introducen en cada botón a modo de selector de valores, asi como permitir una gran personalización del widget. 

## Inicialización del componente: 
Para inicializar el componente, se cuenta con el siguiente constructor: 
`ValueSelectorWidget(color,bgcolor,text,color2,bgcolor2,text2,animWidgColor, height, width)` 
 
Tomando en caso de no inicializarse los atributos los siguientes valores: 

color/color2 = "blue". Esto inicializa los colores de la letra de los botones 1 y 2 respectivamente a azul. </br> 
bgcolor/bgcolor2 = "white". Esto inicializa los colores de fondo de los botones 1 y 2 respectivamente a blanco.  </br>
text/text2 = "texto" y "texto2" respectivamente. Esto inicializa el texto que contendrán los botones a los valores previamente dichos. </br>
animWidgColor = "black". Esto inicializa el color del widget que se encarga de seleccionar los valores a negro. </br>
height/width = 100. Esto inicializa el tamaño tanto de altura como de anchura respectivamente, ambos tomando 100px como valor base. </br>

## Atributos 
Aparte de los atributos previamente mencionados, tenemos el atributo 'selectedVal', el cual seleccionará como valor el valor del texto del botón que se mantiene visible. 

## Métodos: 
`animation()`: Este método se encarga de ejecutar el movimiento que hace el animWidget del boton 1 al 2. Se ejecuta al pulsarse el boton2, y cambia el valor de selectedVal al valor que tenga el texto del boton1 </br></br>
`animation2()`: Este método se encarga de ejecutar el movimiento que hace el animWidget del boton 2 al 1. Se ejecuta al pulsarse el boton1, y cambia el valor de selectedVal al valor que tenga el texto del boton2 </br></br>
`setBoton1TextColor(color)`: Este metodo recibe un String (es valido tanto un valor hexadecimal de un color como un literal de un color) y cambia el color del texto del boton1 a este color </br></br>
`setBoton2TextColor(color)`: Este metodo recibe un String (es valido tanto un valor hexadecimal de un color como un literal de un color) y cambia el color del texto del boton2 a este color </br></br>
`getBoton1TextColor()`: Este metodo devuelve como un String el color que tenga el texto del boton1 </br></br>
`getBoton2TextColor()`: Este metodo devuelve como un String el color que tenga el texto del boton2 </br></br>
`setBoton1BackgroundColor(color)`:  Este metodo recibe un String (es valido tanto un valor hexadecimal de un color como un literal de un color) y cambia el color del fondo del boton1 a este color </br></br>
`setBoton2BackgroundColor(color)`:  Este metodo recibe un String (es valido tanto un valor hexadecimal de un color como un literal de un color) y cambia el color del fondo del boton2 a este color </br></br>
`getBoton1BackgroundColor()`: Este metodo devuelve como un String el color que tenga el fondo del boton1 </br></br>
`getBoton2BackgroundColor()`: Este metodo devuelve como un String el color que tenga el fondo del boton2 </br></br>
`setBoton1Text(texto)`: Este metodo recibe un String y cambia el texto que contiene el boton1 por este String. </br></br>
`setBoton2Text(texto)`: Este metodo recibe un String y cambia el texto que contiene el boton2 por este String. </br></br>
`getBoton1Text()`: Este metodo devuelve un String con el texto que contiene el boton1 </br></br> 
`getBoton2Text()`: Este metodo devuelve un String con el texto que contiene el boton2</br></br> 
`setAnimWidgetBackgroundColor(color)`: Este metodo cambia el color del widget selector por el color (ya sea mediante un hexadecimal o mediante un literal) especificado.</br></br>
`getAnimWidgetBackgroundColor()`: Este metodo devuelve el color del widget selector como un String.

pip install ValueSelectorWidget-MarioRJ2002
