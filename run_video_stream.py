from valy import InputPipeline, DisplayVideo
from pathlib import Path


def main():
    video_path = "movies/MOT16-03-raw.webm"
    input_pipeline = InputPipeline(Path(video_path))
    display_pipeline = DisplayVideo("vis_image")

    pipeline = input_pipeline | display_pipeline

    try:
        for _ in pipeline:
            pass
    except StopIteration:
        return
    except KeyboardInterrupt:
        return
    finally:
        input_pipeline.cleanup()


main()
