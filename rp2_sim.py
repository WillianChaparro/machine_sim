def asm_pio(*args, **kwargs):
    def decorador(programa):
        def compilador():
            print("Parámetros", kwargs) 
            programa()
            return None
        return compilador
    return decorador

def decorador_instr(fun_inst): # Decorador de la funcion decoracion_inst
    def decoracion_instr(self,*args, **kwargs):
        fun_inst(self,*args, **kwargs)
        return None 
    return decoracion_instr

pins='pins' # Se define Pins

class PIO(): # Definicion de clase de la PIO
    OUT_LOW='PIO.OUT_LOW'
    

class StateMachine: #Se define la maquina de estados
  def __init__(self, id_, program, freq=125000000, **kwargs):
        global sm_iniciandose,fsms
        sm_iniciandose=self
        #print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        sm_iniciandose=None
        fsms[id_]=self
        pass
      
        
  def active(self, x=None):# Funcion que simula la Maquina de estados 
    '''Esta rutina simula exclisivamnte esa FSM. Sería interesante crear simulación en paralelo con otras FSM'''
    if x==1:
        print('Está pendiente de realizar la simulación del programa') # Se adicionan ..del programa

fsms=[None]*8 # Se crea lista de 8 elementos en NONE, para cada una de las maquinas de estados

sm_iniciandose=None  # Se inicializa la variable de maquina de estados con None  


class nop: # SE define clase NOP
    @decorador_instr
    def __init__(self,*args, **kwargs):
        global sm_iniciandose
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass
     
    def __getitem__(self,name): # Funcion que llama el item en el que va la instrucción cuando tiene []
        #print('nop.__getattr__',name)
        pass
        
class set(nop): # Se define clase set
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
   
class wrap_target(nop): #Se define la funcion WRAP Target
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs) 
         pass 
  
class wrap(nop):
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass 
         
         
