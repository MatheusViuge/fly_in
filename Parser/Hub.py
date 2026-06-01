class hub:
	def __init__(self, metadata: dict):
		self.metadata = metadata
	
	def start_hub(self):
		if self.metadata is not None:
			print(f"Hub metadata: {self.metadata}")
			dict_keys = list(self.metadata.keys())
			
			if dict_keys[0] != "start_hub":
				print("[Error]: Invalid metadata keys")
				return

			dict_values = list(self.metadata.values())
			dados = tuple(dict_values[0].split(","))
			
			#tratamento para verificar se existe caracter invalido no nome
			for i in dados[0]:
				if (i == "-" or i == " "):
					print("[Error]: Name invalid")
					return
			
			

	def end_hub(self):
		pass
	



hub1 = hub({"start_hub": "start,0,0,[color=green,max_drones=6]"})

hub1.start_hub()