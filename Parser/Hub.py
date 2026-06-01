class hub:
	def __init__(self, metadata: dict):
		self.metadata = metadata
	
	def start_hub(self):
		if self.metadata is not None:
			print(f"Hub metadata: {self.metadata}")
			dict_keys = list(self.metadata.keys())
			
			if dict_keys[0] != "start_hub":
				raise ValueError("[Error]: Invalid metadata keys")

			dict_values = list(self.metadata.values())
			dados = tuple(dict_values[0].split(","))
			
			#tratamento para verificar se existe caracter invalido no nome
			for i in dados[0]:
				if (i == "-" or i == " "):
					raise ValueError("[Error]: Name invalid")
			
			#tratamento para verificar se existe valores invalidos
			try:
				dados[1] = int(dados[1]) if isinstance(dados[1], str) else dados[1]
				dados[2] = int(dados[2]) if isinstance(dados[2], str) else dados[2]
			except ValueError:
				raise ValueError("[Error]: Invalid data types")
			
			
			

	def end_hub(self):
		pass
	



hub1 = hub({"start_hub": "start,0,0,[color=green,max_drones=6]"})

hub1.start_hub()