import json
import datetime
import boto3
import csv
import tempfile

def formato(dic):
  todos = [["FechaDescarga","Barrio", "Precio", "Estrato", "NumHabitaciones", "NumBanos", "mts2"]]
  actual = datetime.datetime.now()
  interes = [['locations', 'neighbourhoods', 'name'],['price'], ['stratum', 'name'],['rooms', 'name'], ['baths', 'name'],['area']]
  tam = len(dic['hits']['hits'])
  for k in range(tam):
    ims = dic['hits']['hits'][k]['_source']['listing']
    info = [f"{actual.year}-{actual.strftime('%m')}-{actual.strftime('%d')}"]
    for i in interes:
      for j in range(len(i)):
        sel = [[ims[i[j]][0] if type(ims.get(i[j])) == list else ims.get(i[j], ims)][0] if j ==0 else [sel[i[j]][0] if type(sel.get(i[j])) == list else sel.get(i[j], sel)][0]][0]
      info.append(sel)
    todos.append(info)
  return todos
  
  
  
def lambda1(event, context):
    nuevo = event['Records'][0]['s3']['object']['key']
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('bucketparcial2')
    obj = bucket.Object(nuevo)
    body = obj.get()['Body'].read()
    info = json.loads(body)
    print(f"Informacion{info}")
    info2 = formato(info)
    
    client = boto3.client('s3')
    nombre = nuevo.split(".")[0]+".csv"
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        writer = csv.writer(temp_file, delimiter=',')
        writer.writerows(info2)
        temp_file.close()
    
        with open(temp_file.name, 'rb') as f:
            client.put_object(Body=f, Bucket='bucketparcial3', Key=nombre)
    return {
        'statusCode': 200,
        'body': json.dumps('Final')
    }