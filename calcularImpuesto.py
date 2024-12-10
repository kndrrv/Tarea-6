class CalculadorImpuestos:
    def calcular_impuesto(self, estado, monto):
        estado = estado.upper()
        
        # NH no tiene impuestos
        if estado == 'NH':
            return 0
        
        # MA, CA y TX tienen 18%
        if estado in ['MA', 'CA', 'TX']:
            return monto * 0.18
        
        # IL y KY escalonados
        if estado in ['IL', 'KY']:
            if monto < 1000:
                return 0
            elif 1000 <= monto <= 10000:
                return monto * (0.12 if estado == 'IL' else 0.13)
            else:  # monto > 10000
                return monto * (0.16 if estado == 'IL' else 0.17)
        
        # Resto de estados 
        return monto * 0.15