from google.colab import drive
pathTrain = '/content/CNN/train'
pathTest = '/content/CNN/test'


if (os.path.exists(pathTrain) and os.path.exists(pathTest)):
    print('OK')
else:
    print('No existen carpetas')
    print('Copiando...')
    
    drive.mount('/gdrive', force_remount=True)
    
    path_drive = '/gdrive/MyDrive/IA/CNN'
    local_path = '/content'
    !cp -r '{path_drive}' '{local_path}'
    print ('Copiados ')