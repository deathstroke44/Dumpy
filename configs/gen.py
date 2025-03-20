s="[[dataset-name]]\ntsLength = [len]\nmaxK = [k]\npaafn = /data/kabir/similarity-search/dumpy-output-files/paa/[dataset-name]-16.bin\nsaxfn = /data/kabir/similarity-search/dumpy-output-files/sax/[dataset-name]-16.bin\nidxfn = /data/kabir/similarity-search/dumpy-output-files/non-mat/[dataset-name]-16.bin_le\nfuzzyidxfn = /data/kabir/similarity-search/dumpy-output-files/fuzzy-index/[dataset-name]/\nmemoryidxfn = /data/kabir/similarity-search/dumpy-output-files/memory/[dataset-name]/\ndatafn = /data/kabir/similarity-search/dataset/[dataset-name]/base.fvecs\nqueryfn = /data/kabir/similarity-search/dataset/[dataset-name]/query.fvecs\n"

datasets=[('astro1m',256,100),('audio',192, 20),('bigann',128,100),('cifar',512,20),('deep',256,20),('enron',1369,20),('gist',960, 100),('glove',100,20),('imageNet',150,20),('lastfm',65,100),('millionSong',420,20),('movielens',150,100),('MNIST',784,20),('netflix',300,100),('notre',128,20),('nuswide',500,20),('nytimes',256,100),('random', 100, 20),('sald1m', 128, 100),('seismic1m', 256, 100),('sift', 128, 100),('space1V', 100, 100),('sun', 512, 20),('text-to-image', 200, 100),('tiny5m', 384, 100),('trevi',4096, 20),('uqv', 256, 100),('ukbench', 128, 20),('word2vec', 300, 100),('yahoomusic', 300, 100),('ethz', 256, 100),('vcseis', 256, 100),('txed', 256, 100),('lendb', 256, 100),('stead', 256, 100),('geofon', 128, 100),('instancegm', 128, 100),('Music', 100, 100),('Yelp', 50, 100)]







for dataset in datasets:
    p=s+''
    p=p.replace('[dataset-name]',dataset[0])
    p=p.replace('[len]',str(dataset[1]))
    p=p.replace('[k]',str(dataset[2]))
    print(p)

# for dataset in datasets:
#     print('mkdir '+dataset[0]+' && ',end='')
# print('echo 1')