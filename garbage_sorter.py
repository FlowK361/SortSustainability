import cohere

var = input('What you want to dispose?')
co = cohere.Client('lq3FAyDUXvcBcJZ1CrWGPVJ1iCXBeD06o83lrach') # This is your trial API key
response = co.generate(
  model='command',
  prompt=f'Where can I dispose of a {var} peel? possible options would be recycling, trash, green bin, compost',
  max_tokens=500,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))