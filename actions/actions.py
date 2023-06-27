from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random
import webbrowser


class ActionGiveExercise(Action):
    
    def name(self) -> Text:
        return "action_give_exercise"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        top = tracker.get_slot("topic")
        optionsAR = ['Tenemos un elemento de número atómico Z = 16. ¿Será mayor su radio atómico o su radio iónico?','Determine el radio iónico y atómico de los siguientes elementos: a) F b) He c) Be d) Rf','Determine el radio iónico y atómico de los siguientes elementos: a) Ta b) Re c) Nb d) Cn']
        optionsS = ['El tetrahidrocannabinol (THC) es una sustancia tóxica. Con muy poca cantidad (2,5 . 10 ^ -5 g)se produce una intoxicación. Su fórmula molecular es C21H33O2. a) Cuántos moles de THC representa el mínimo necesario para que se produzca una intoxicación? b) Cuántas moléculas representan?','Dónde habrá mayor número de átomos, en 1 mol de Metanol o en un Mol de ácido metanoico?','Dada la reacción: Zn+2HCl ----> ZnCl2 +H2 ¿Cuántos moles de ZnCl2 se producirán a partir de 55.0 g de Zn, si suponemos que el HCl está disponible en exceso?']
        optionsLE = ['Graficar la estructura de lewis de los siguientes compuestos: a) CO2 b) H2SO4 c) O2 d) CO e) NO2','Graficar la estructura de lewis de los siguientes compuestos: a) NO b) H2O c) NO3– d) H3PO4','Graficar la estructura de lewis de los siguientes compuestos: a) K2SO4 b) H2O2 c) NaCl d) CCl4']
        optionsCB = ['Indique las características que deben poseer dos átomos para formar un enlace Covalente Apolar.','En lugar de aportar un electrón cada átomo del enlace, los dos electrones son aportados por el mismo átomo. Este tipo de enlace recibe el nombre de enlace covalente coordinado o enlace covalente dativo. Realizar el esquema para los siguientes compuestos, e indicar el número de enlaces simples, dobles, dativos. a) SO2 b) NH3','Dado los siguientes compuestos, agrupar de acuerdo a si tienen enlace covalentes simples, dobles o triples. a) H2 b) Cl2 c) O2 d) N2 e) F2 f)CO2 g) H2O h) HNO2 i) HCl j) CO']
        optionsIB = ['De el nombre de cinco metales y no metales que puedan formar enlaces iónicos con facilidad. Escriba las fórmulas y los nombres de los compuestos que se formarían al combinar los elementos mencionados.','Explica la formación de los siguientes enlaces iónicos: a) El Na( Z=11) con el Cl (Z=17) b) El Mg(Z=12) con el F (Z=9) c) El K(Z=19) con el N (Z=7)','Indique cuales de las siguientes moléculas poseen un enlace iónico: a) KBr b) CO c) Ión Amonio d) O2']
        global exercise
        exercise = "No tengo"
        if top.lower() == "radio atomico":
            exercise = random.choice(optionsAR)
        elif top.lower() == "estequiometria":
            exercise = random.choice(optionsS)
        elif top.lower() == "estructura de lewis":
            exercise = random.choice(optionsLE)
        elif top.lower() == "enlace covalente":
            exercise = random.choice(optionsCB)
        elif top.lower() == "enlace ionico":
            exercise = random.choice(optionsIB)
                    
        dispatcher.utter_message(text=exercise)     
        
        return []

class ActionCustomGoodbye(Action):

    def name(self) -> Text:
        return "action_custom_goodbye"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mood = tracker.get_slot("mood")
        name = tracker.get_slot("name")
        if name is None:
            if mood == "happy":
                dispatcher.utter_message("Nos vemos! Que sigas bien!")
            elif mood == "sad":
                dispatcher.utter_message("Nos vemos. Espero que te sientas mejor.")
            elif mood == "angry":
                dispatcher.utter_message("Nos vemos. Ojala haya podido ser de ayuda.")
            elif mood is None:
                dispatcher.utter_message("Nos vemos!")
        else:
            if mood == "happy":
                dispatcher.utter_message("Nos vemos, {}! Que sigas bien!".format(name))
            elif mood == "sad":
                dispatcher.utter_message("Nos vemos, {}. Espero que te sientas mejor.".format(name))
            elif mood == "angry":
                dispatcher.utter_message("Nos vemos, {}. Ojala haya podido ser de ayuda.".format(name))
            elif mood is None:
                dispatcher.utter_message("Nos vemos, {}!".format(name))
                
        return[]
        

class ActionGiveVideo(Action):
    
    def name(self) -> Text:
        return "action_give_video"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        top = tracker.get_slot("topic")
        optionsAR = ['https://www.youtube.com/watch?v=X47LBV4jJ8A','https://www.youtube.com/watch?v=0uyT9e_MDeQ','https://www.youtube.com/watch?v=BC24pwVlf9g','https://www.youtube.com/watch?v=kq0VamBdANY','https://www.youtube.com/watch?v=cwBcyp9NlaA']
        optionsS = ['https://www.youtube.com/watch?v=uybirxYQEvQ','https://es.khanacademy.org/science/ap-chemistry/stoichiometry-and-molecular-composition-ap/stoichiometry-ideal-ap/v/stoichiometry','https://www.youtube.com/watch?v=olgYihEe6B8','https://www.youtube.com/watch?v=RxVfUhutNyM','https://www.youtube.com/watch?v=Mzvq-IboKSM']
        optionsLE = ['https://www.youtube.com/watch?v=dWh4wf5VgMs','https://www.youtube.com/watch?v=cYRlVodmaJU','https://www.youtube.com/watch?v=ttNWZ1cbs34','https://www.youtube.com/watch?v=5gcWhCfASx0','https://www.youtube.com/watch?v=IXQ0amr_u3I']
        optionsCB = ['https://es.khanacademy.org/science/ap-biology/chemistry-of-life/introduction-to-biological-macromolecules/v/covalent-bonds','https://www.youtube.com/watch?v=WnVFcnGvJ-Y','https://www.youtube.com/watch?v=cvMoYI1cDFg','https://www.youtube.com/watch?v=rtuFNybKMTs','https://www.youtube.com/watch?v=9sjC6K6TAH8']
        optionsIB = ['https://es.khanacademy.org/science/ap-biology/chemistry-of-life/introduction-to-biological-macromolecules/v/ionic-bonds','https://www.youtube.com/watch?v=WnVFcnGvJ-Y','https://www.youtube.com/watch?v=51tkpoScWXs','https://www.youtube.com/watch?v=hd1eTxqozSs','https://www.youtube.com/watch?v=rhx8T5fDUU0']
        global video_url
        video_url = "No tengo"
        if top.lower() == "radio atomico":
            video_url = random.choice(optionsAR)
        elif top.lower() == "estequiometria":
            video_url = random.choice(optionsS)
        elif top.lower() == "estructura de lewis":
            video_url = random.choice(optionsLE)
        elif top.lower() == "enlace covalente":
            video_url = random.choice(optionsCB)
        elif top.lower() == "enlace ionico":
            video_url = random.choice(optionsIB)
                    
        dispatcher.utter_message("Reproduciendo el video pedido...")     
        
        webbrowser.open(video_url)
        
        return []

class ActionTopicExplanation(Action):
        
    def name(self) -> Text:
        return "action_topic_explanation"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        top = tracker.get_slot("topic")
        optionsAR = ['El radio atómico identifica la distancia que existe entre el núcleo, y el orbital más externo de un átomo. Por medio del radio atómico, es posible determinar el tamaño del átomo.El radio iónico es, al igual que el radio atómico, la distancia entre el centro del núcleo del átomo y el electrón estable más alejado del mismo, pero haciendo referencia no al átomo, sino al ion. Este aumenta en la tabla de derecha a izquierda en los periodos y de arriba hacia abajo en los grupos.','El radio atómico identifica la distancia que existe entre el núcleo, y el orbital más externo de un átomo. Por medio del radio atómico, es posible determinar el tamaño del átomo. El radio iónico es, al igual que el radio atómico, la distancia entre el centro del núcleo del átomo y el electrón estable más alejado del mismo, pero haciendo referencia no al átomo, sino al ión. En el caso de cationes, la ausencia de uno o varios electrones diminuye la fuerza eléctrica de repulsión mutua entre los electrones restantes, provocando el acercamiento de los mismos entre sí y al núcleo positivo del átomo del que resulta un radio iónico menor que el atómico. En el caso de los aniones, el fenómeno es el contrario, el exceso de carga eléctrica negativa obliga a los electrones a alejarse unos de otros para restablecer el equilibrio de fuerzas eléctricas, de modo que el radio iónico es mayor que el atómico.']
        optionsS = ['En química, la estequiometría  es el cálculo de las relaciones cuantitativas entre los reactivos y productos en el transcurso de una reacción química.','La estequiometría expresa al relación cuantitativa entre los reactivos y los productos en una ecuación química. Los coeficientes estequiométricos en una ecuación balanceada indican las proporciones molares en esa reacción. La estequiometría nos permite predecir ciertos valores, tales como el porcentaje de rendimiento de un producto o la masa molar de un gas.','La estequiometría es el cálculo para una ecuación química balanceada que determinará las proporciones entre reactivos y productos en una reacción química. El balance en la ecuación química obedece a los principios de conservación y los modelos atómicos de Dalton como, por ejemplo, la Ley de conservación de masa que estipula que la masa de los reactivos es igual a la masa de los productos. En este sentido, la ecuación debe tener igual peso en ambos lados de la ecuación. ']
        optionsLE = ['La estructura de Lewis, también llamada diagrama de punto y raya diagonal, modelo de Lewis, diagrama de Valencia o regla de Octeto es una representación gráfica que muestra los pares de electrones en guiones o puntos de enlaces entre los átomos de una molécula y los pares de electrones solitarios que puedan existir.2 Son representaciones bidimensionales sencillas de la conectividad de los átomos en las moléculas; así como de la posición de los electrones enlazantes y no enlazantes. En esta fórmula se muestran enlaces químicos dentro de la molécula, ya sea explícitamente o implícitamente indicando la ordenación de los átomos en el espacio. Esta representación se usa para saber la cantidad de electrones de valencia que puedan existir en un elemento que interactúan con otros o entre su misma especie, formando enlaces ya sea simples, dobles, o triples los cuales se encuentran íntimamente relacionados con la geometría molecular.','Estructura de Lewis, también llamada diagrama de punto, modelo de Lewis o representación de Lewis, es una representación gráfica que muestra los enlaces entre los átomos de una molécula y los pares de electrones solitarios que puedan existir. Esta representación se usa para saber la cantidad de electrones de valencia de un elemento que interactúan con otros o entre su misma especie, formando enlaces ya sea simples, dobles, o triples y estos se encuentran íntimamente en relación con los enlaces químicos entre las moléculas y su geometría molecular, y la distancia que hay entre cada enlace formado.','Las estructuras, diagramas o fórmulas de Lewis de una molécula son representaciones bidimensionales sencillas del esqueleto o conectividad de los átomos en la molécula y de la posición de los electrones enlazantes y no enlazantes. Tienen como finalidad explicar el enlace covalente mediante la compartición de uno o más pares de electrones entre dos átomos con el objeto de cerrar capa y conseguir así la máxima estabilidad. En ella, dichos enlaces y los electrones se representan con puntos o guiones largos, aunque la mayoría de las veces los puntos corresponden a los electrones no compartidos y los guiones a los enlaces covalentes.']
        optionsCB = ['Se llama enlace covalente a un tipo de enlace químico, que ocurre cuando dos átomos se enlazan para formar una molécula, compartiendo electrones pertenecientes de su capa más superficial, alcanzando gracias a ello el conocido “octeto estable” (conforme a la “regla del octeto” propuesto por Gilbert Newton Lewis sobre la estabilidad eléctrica de los átomos). Los átomos así enlazados comparten un par (o más) de electrones, cuya órbita varía y se denomina orbital molecular. En los Enlaces covalentes polares Se enlazan átomos de distintos elementos y con diferencia de electronegatividad por encima de 0,5. Así se forman dipolos electromagnéticos. En los Enlaces covalentes no polares se enlazan átomos de un mismo elemento o de idénticas polaridades, con una diferencia de electronegatividad muy pequeña (menor a 0,4). La nube electrónica, así, es atraída con igual intensidad por ambos núcleos y no se forma un dipolo molecular. Características: 1) Están formados por no metal + no metal. 2) Forman moléculas verdaderas. 3) Los no metales comparten electrones.','Los enlaces covalentes son las fuerzas que mantienen unidos entre sí los átomos no metálicos (los elementos situados a la derecha en la tabla periódica -C, O, F, Cl, ...). Estos átomos tienen muchos electrones en su nivel más externo (electrones de valencia) y tienen tendencia a ganar electrones más que a cederlos, para adquirir la estabilidad de la estructura electrónica de gas noble. Por tanto, los átomos no metálicos no pueden cederse electrones entre sí para formar iones de signo opuesto. En este caso el enlace se forma al compartir un par de electrones entre los dos átomos, uno procedente de cada átomo. El par de electrones compartido es común a los dos átomos y los mantiene unidos, de manera que ambos adquieren la estructura electrónica de gas noble. Se forman así habitualmente moléculas, pequeños grupos de átomos unidos entre sí por enlaces covalentes. En los Enlaces no polares, los átomos que se unen tienen la misma electronegatividad o su diferencia es baja (menor a 0,4). En los Enlaces polares, los átomos que se unen tienen una diferencia de electronegatividad mayor a 0,4 (hasta 1,7-1,8). Características: 1) Están formados por no metales + no metal. 2) Forman moléculas verdaderas. 3)Los no metales comparten electrones.','En los enlaces covalentes se comparten pares de electrones entre los átomos. Si los pares de electrones se comparten entre átomos con electronegatividad igual o muy similar se forma un enlace covalente no polar (por ejemplo, H-H, o C-H), y si los electrones se comparten entre átomos con electronegatividad desigual, se forman enlaces covalentes polares (tal como H-O). En los enlaces no polares, Los átomos que se unen tienen la misma electronegatividad o su diferencia es baja (menor a 0,4). En los enlaces polares, los átomos que se unen tienen una diferencia de electronegatividad mayor a 0,4 (hasta 1,7-1,8). Características: 1) Están formados por no metal + no metal. 2) Forman moléculas verdaderas. 3) Los no metales comparten electrones.']
        optionsIB = ['Los enlaces iónicos son el resultado de la atracción electrostática entre iones con cargas opuestas que se forman cuando se transfieren electrones de valencia de un átomo a otro. Enlace iónico o electrovalente. Es una unión de partículas que resulta de la presencia de atracción electrostática entre los iones de distinto signo, es decir, uno fuertemente electropositivo (baja energía de ionización) y otro fuertemente electronegativo (alta afinidad electrónica). Eso se da cuando en el enlace, uno de los átomos capta electrones del otro. Cuando una sustancia contiene átomos de metales y no metales, los electrones son atraídos con más fuerza por los no metales, elementos de elevadas electronegatividades y afinidad electrónica, los cuales se transforman en iones con carga negativa; los metales, con energía de ionización pequeña, a su vez, se convierten en iones con carga positiva. Características: 1) Está formado por metal + no metal. 2) No forma moléculas verdaderas, existe como un agregado de aniones (iones negativos) y cationes (iones positivos). 3) Los metales ceden electrones formando cationes, los no metales aceptan electrones formando aniones.','Un enlace iónico o electrovalente es el resultado de la presencia de atracción electrostática entre los iones de distinto signo respecto a las valencias de los elementos y el número de electrones que deben perder o ganar para completar las capas, es decir, uno fuertemente electropositivo y otro fuertemente electronegativo. Eso se da cuando en el enlace, uno de los átomos capta electrones del otro. La atracción electrostática entre los iones de carga opuesta causa que se unan y formen un compuesto químico simple, aquí no se fusionan; sino que uno da y otro recibe. Para que un enlace iónico se genere es necesario que la diferencia (delta) de electronegatividades sea mayor que 1,7 o igual.','Se entiende por enlace iónico o enlace electrovalente a uno de los mecanismos de unión química, que se da generalmente entre átomos metálicos y no metálicos, fusionados debido a la transferencia permanente de electrones, y produciendo así una molécula cargada electromagnéticamente, conocida como ion. La transferencia electrónica en el enlace iónico se da siempre desde los átomos metálicos hacia los no metálicos, o en todo caso, desde los más electronegativos hacia los menos. Esto se debe a que la juntura se produce por atracción entre partículas de distinto signo, cuya variación en el coeficiente de electronegatividad sea mayor o igual a 1,7 en la escala de Pauling.']
        global explanation
        explanation = "No lo se"
        if top.lower() == "radio atomico":
            explanation = random.choice(optionsAR)
        elif top.lower() == "estequiometria":
            explanation = random.choice(optionsS)
        elif top.lower() == "estructura de lewis":
            explanation = random.choice(optionsLE)
        elif top.lower() == "enlace covalente":
            explanation = random.choice(optionsCB)
        elif top.lower() == "enlace ionico":
            explanation = random.choice(optionsIB)
                    
        dispatcher.utter_message(text=explanation)     
        
        return []
