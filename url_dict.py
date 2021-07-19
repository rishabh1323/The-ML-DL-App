root_url = "https://the-ml-dl-app-bucket.s3.amazonaws.com/static/statistics_images/"

url_dict = {
    # House Price Prediction
    '1' : {
        "source_code_link" : "https://github.com/rishabh1323/House-Price-Prediction",
        "dataset_link" : "https://www.kaggle.com/c/house-prices-advanced-regression-techniques",
        "stats_images_list" : {
            "Bar Plots" : [
                f"{root_url}1_bar_1.png", f"{root_url}1_bar_2.png",
                f"{root_url}1_bar_3.png", f"{root_url}1_bar_4.png",
                f"{root_url}1_bar_5.png", f"{root_url}1_bar_6.png",
                f"{root_url}1_bar_7.png", f"{root_url}1_bar_8.png",
                f"{root_url}1_bar_9.png", f"{root_url}1_bar_10.png"
            ],
            "Box Plots" : [
                f"{root_url}1_box_1.png", f"{root_url}1_box_2.png",
                f"{root_url}1_box_3.png", f"{root_url}1_box_4.png",
                f"{root_url}1_box_5.png", f"{root_url}1_box_6.png",
                f"{root_url}1_box_7.png", f"{root_url}1_box_8.png",
                f"{root_url}1_box_9.png", f"{root_url}1_box_10.png"
            ],
            "Scatter Plots" : [
                f"{root_url}1_scatter_1.png", f"{root_url}1_scatter_2.png",
                f"{root_url}1_scatter_3.png"
            ],
            "Distibution Plots" : [
                f"{root_url}1_dist_1.png", f"{root_url}1_dist_2.png",
                f"{root_url}1_dist_3.png"
            ]
        }
    },
    # Digit Recognition
    '2' : {
        "source_code_link" : "https://github.com/rishabh1323/Deep-Learning-Basic-Projects/tree/main/MNIST%20Digit%20Recognition",
        "dataset_link" : "https://www.kaggle.com/scolianni/mnistasjpg",
        "test_images_link" : "https://archive.org/download/mnist_digit_recognizer_dataset/test.zip/",
        "stats_images_list" : {
            "Graphs" : [
                f"{root_url}2_graph_1.png", f"{root_url}2_graph_2.png"
            ],
            "Scalars" : [
                f"{root_url}2_scalar_1.png", f"{root_url}2_scalar_2.png"
            ],
            "Distributions" : [
                f"{root_url}2_dist_1.png", f"{root_url}2_dist_2.png",
                f"{root_url}2_dist_3.png", f"{root_url}2_dist_4.png",
                f"{root_url}2_dist_5.png", f"{root_url}2_dist_6.png",
                f"{root_url}2_dist_7.png", f"{root_url}2_dist_8.png",
                f"{root_url}2_dist_9.png", f"{root_url}2_dist_10.png"
            ],
            "Histograms" : [
                f"{root_url}2_hist_1.png", f"{root_url}2_hist_2.png",
                f"{root_url}2_hist_3.png", f"{root_url}2_hist_4.png",
                f"{root_url}2_hist_5.png", f"{root_url}2_hist_6.png",
                f"{root_url}2_hist_7.png", f"{root_url}2_hist_8.png",
                f"{root_url}2_hist_9.png", f"{root_url}2_hist_10.png"
            ]
        }
    },
    # Rock Paper Scissors
    '3' : {
        "source_code_link" : "https://github.com/rishabh1323/Deep-Learning-Basic-Projects/tree/main/Rock%20Paper%20Scissors",
        "dataset_link" : "https://laurencemoroney.com/datasets.html#rock-paper-scissors-dataset",
        "test_images_link" : "https://archive.org/download/rock-paper-scissors-dataset/rps-test-set.zip/",
        "stats_images_list" : {
            "Graphs" : [
                f"{root_url}3_graph_1.png", f"{root_url}3_graph_2.png"
            ],
            "Scalars" : [
                f"{root_url}3_scalar_1.png", f"{root_url}3_scalar_2.png",
                f"{root_url}3_scalar_3.png", f"{root_url}3_scalar_4.png"
            ],
            "Distributions" : [
                f"{root_url}3_dist_1.png", f"{root_url}3_dist_2.png",
                f"{root_url}3_dist_3.png", f"{root_url}3_dist_4.png",
                f"{root_url}3_dist_5.png", f"{root_url}3_dist_6.png",
                f"{root_url}3_dist_7.png", f"{root_url}3_dist_8.png",
                f"{root_url}3_dist_9.png", f"{root_url}3_dist_10.png",
                f"{root_url}3_dist_11.png", f"{root_url}3_dist_12.png"
            ],
            "Histograms" : [
                f"{root_url}3_hist_1.png", f"{root_url}3_hist_2.png",
                f"{root_url}3_hist_3.png", f"{root_url}3_hist_4.png",
                f"{root_url}3_hist_5.png", f"{root_url}3_hist_6.png",
                f"{root_url}3_hist_7.png", f"{root_url}3_hist_8.png",
                f"{root_url}3_hist_9.png", f"{root_url}3_hist_10.png",
                f"{root_url}3_hist_11.png", f"{root_url}3_hist_12.png"
            ]
        }
    },
    # Bank Note Authentication
    '4' : {
        "source_code_link" : "https://github.com/rishabh1323/Bank-Note-Authentication",
        "dataset_link" : "https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data",
        "stats_images_list" : {
            "Box Plots" : [
                f"{root_url}4_box_1.png", f"{root_url}4_box_2.png",
                f"{root_url}4_box_3.png", f"{root_url}4_box_4.png"
            ],
            "Count Plots" : [
                f"{root_url}4_count_1.png"
            ],
            "Distibution Plots" : [
                f"{root_url}4_dist_1.png", f"{root_url}4_dist_2.png",
                f"{root_url}4_dist_3.png", f"{root_url}4_dist_4.png"
            ]
        }
    },
    # Car Resale Value
    '5' : {
        "source_code_link" : "https://github.com/rishabh1323/Car-Resale-Value-Prediction",
        "dataset_link" : "https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho",
        "stats_images_list" : {
            "Bar Plots" : [
                f"{root_url}5_bar_1.png", f"{root_url}5_bar_2.png",
                f"{root_url}5_bar_3.png", f"{root_url}5_bar_4.png"
            ],
            "Box Plots" : [
                f"{root_url}5_box_1.png", f"{root_url}5_box_2.png",
                f"{root_url}5_box_3.png", f"{root_url}5_box_4.png"
            ],
            "Scatter Plots" : [
                f"{root_url}5_scatter_1.png", f"{root_url}5_scatter_2.png"
            ],
            "Distibution Plots" : [
                f"{root_url}5_dist_1.png", f"{root_url}5_dist_2.png",
                f"{root_url}5_dist_3.png", f"{root_url}5_dist_4.png"
            ]
        }
    }   
}