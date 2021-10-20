from os import path

TRAIN_IMAGES = "../ch11_GoogLeNet/tiny-imagenet-200/train"
VAL_IMAGES = "../ch11_GoogLeNet/tiny-imagenet-200/val/images"

VAl_MAPPINGS = "../ch11_GoogLeNet/tiny-imagenet-200/val/val_annotations.txt"

WORDNET_IDS = "../ch11_GoogLeNet/tiny-imagenet-200/wnids.txt"
WORD_LABELS = "../ch11_GoogLeNet/tiny-imagenet-200/words.txt"

NUM_CLASSES = 200
NUM_TEST_IMAGES = 50 * NUM_CLASSES

TRAIN_HDF5 = "../ch11_GoogLeNet/tiny-imagenet-200/hdf5/train.hdf5"
VAL_HDF5 = "../ch11_GoogLeNet/tiny-imagenet-200/hdf5/val.hdf5"
TEST_HDF5 = "../ch11_GoogLeNet/tiny-imagenet-200/hdf5/test.hdf5"

DATASET_MEAN = "output/tiny-imagenet-200-mean.json"

OUTPUT_PATH = "output"
MODEL_PATH = path.sep.join([OUTPUT_PATH, "resnet_tinyimagenet.hdf5"])
FIG_PATH = path.sep.join([OUTPUT_PATH, "resnet56_tinyimagenet.png"])
JSON_PATH = path.sep.join([OUTPUT_PATH, "resnet_json_tinyimagenet.json"])








