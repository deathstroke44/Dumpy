import sys

datasets=[('astro1m',256,100,100),('audio',192, 20,200),('bigann',128,100,100),('cifar',512,20,200),('deep',256,20,200),('enron',1369,20,200),('gist',960, 100, 1000),('glove',100,20,200),('imageNet',150,20,200),('lastfm',65,100,100),('millionSong',420,20,200),('movielens',150,100,1000),('MNIST',784,20,200),('netflix',300,100,1000),('notre',128,20,200),('nuswide',500,20,200),('nytimes',256,100,100),('random', 100, 20,200),('sald1m', 128, 100,100),('seismic1m', 256, 100,100),('sift', 128, 100,10000),('space1V', 100, 100,100),('sun', 512, 20,200),('text-to-image', 200, 100,100),('tiny5m', 384, 100,1000),('trevi',4096, 20,200),('uqv', 256, 100, 10000),('ukbench', 128, 20,200),('word2vec', 300, 100,1000),('yahoomusic', 300, 100,100),('ethz', 256, 100,100),('vcseis', 256, 100,100),('txed', 256, 100,100),('lendb', 256, 100,100),('stead', 256, 100,100),('geofon', 128, 100,100),('instancegm', 128, 100,100),('Music', 100, 100,100),('Yelp', 50, 100,100)]
runs=''
for dataset in datasets:
    for i in range(1,5):
        temp_name='config_template_1_step_'+str(i)+'.ini'
        file_name='config_'+dataset[0]+'_1_step_'+str(i)+'.ini'
        with open(temp_name, "r") as file:
            content = file.read()
            s=content+''
            s=s.replace('[dataset-name]', dataset[0])
            s=s.replace('[query_num]', str(dataset[3]))
            sys.stdout = open(file_name, "w")
            print(s)
            runs=runs+'/usr/bin/time -v ./Dumpy '+file_name+' &> '+file_name+'logs.txt ; '
runs=runs+'echo 1'
sys.stdout = open('run_all.sh', "w")
print(runs)