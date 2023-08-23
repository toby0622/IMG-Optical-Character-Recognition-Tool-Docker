import os
import shutil


progress_bar_ratio = 0


# clean up the directory on the website startup
def file_cleanup(directory):
    folder = directory

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


# dynamic progress bar
def progress_bar_calculation(current_images, total_images):
    global progress_bar_ratio

    progress_bar_ratio = current_images / float(total_images)
    progress_bar_ratio = int(round(progress_bar_ratio, 2) * 100)


# value getter for JavaScript
def get_bar_ratio():
    global progress_bar_ratio
    return progress_bar_ratio


def written_default(ocr_results):
    ocr_results = sorted(ocr_results, key=lambda x: (x[0][1][1]), reverse=False)

    return ocr_results


def written_reverse(ocr_results):
    # sorting using recognition box x-axis, from right to left
    ocr_results = sorted(ocr_results, key=lambda x: (x[0][1][0]), reverse=True)

    return ocr_results
