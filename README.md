# WWTPBaseline

[Faster R-CNN pre-trained by Detectron2](https://github.com/facebookresearch/detectron2/blob/main/MODEL_ZOO.md)


## Setup

```bash
docker run --gpus device=1 -d -it --shm-size 32G --mount source=$(pwd),target=/home/appuser/wwtp,type=bind tumbgd/detectron2
docker exec -it <docker-container-id> bash
```

Specify `--gpus device` according to your own machine.

## Step

1. Fix names of test images:

    ```bash
    python fix_test.py
    ```

    Note that only run ONCE.

2. Get results:

    ```bash
    python run.py
    ```


