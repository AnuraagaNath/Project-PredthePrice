
# Project PredthePrice

**Project Description: "Project-PredthePrice"**

As a dedicated Masters student in Data Science, I present "Project-PredthePrice," a meticulously crafted solo endeavor focused on the domain of resale price prediction for automobiles, specifically catering to cars and bikes. This project is characterized by a commitment to precision, data-driven insights, and a comprehensive scope that encompasses both foreign luxury cars and vehicles available in India.

**Key Features:**

1. **Inclusion of Foreign Luxury Cars:**
   - Our project encompasses a diverse range of foreign luxury cars, ensuring a comprehensive analysis of resale price trends in this exclusive automotive segment.

2. **Coverage of Available in India Cars:**
   - Addressing the local context, "Project-PredthePrice" extends its reach to include cars available in India. This integration reflects a nuanced understanding of the unique factors influencing the resale market within the country.

3. **Incorporation of Bikes – Indian and Luxury:**
   - Beyond cars, our project provides a holistic perspective by delving into the resale price prediction for both Indian bikes and luxury motorcycles. This dual focus expands the utility of our models to cater to a broader audience.

4. **Impressive Prediction Scores:**
   - The predictive models employed in "Project-PredthePrice" boast consistently high accuracy scores, ranging between 80% and 96%. This reliability underscores the robustness of our analytical approach and the meticulous methodology applied in developing these models.

**About the Car Type Detection Model**
A dataset named "Vehicle Type Image Dataset (Version 2): VTID2," consisting of approximately 3000 images sourced from an open data repository, was utilized for training a model. The dataset citation is provided as:

Boonsirisumpun, Narong; surinta, olarik (2021), “Vehicle Type Image Dataset (Version 2): VTID2”, Mendeley Data, V2, doi: 10.17632/htsngg9tpc.2

The image training process involved using Support Vector Machines (SVM) with impressive accuracy rates of 99.8% for training and 99.3% for testing. The images were categorized into four types: "Hatchback," "Pickup," "SUV," and "Sedan." Prior to training, the images were converted to flattened 28 × 28 pixels and then used to fine-tune the model.

The resulting model was integrated into a web application, which showcases the predicted class's probability. A notable feature of the web app is the inclusion of an animated progress bar that enhances the user interface, providing visual feedback on the prediction process.

**Future Expansion:**
As the project evolves, I envision its expansion to include additional commodities beyond cars and bikes. This strategic roadmap aligns with my commitment to continuous improvement and adaptability to emerging data science challenges. Also, the data will be live scrapped from websites for more relevancy.

**About the Developer:**
"Project-PredthePrice" is the culmination of my pursuit of excellence in the field of data science. As a solo project, it reflects not only my technical proficiency but also a passion for leveraging data to derive meaningful insights. My academic background serves as a strong foundation, ensuring a rigorously analytical and evidence-based approach to resale price prediction.

In conclusion, "Project-PredthePrice" stands as a testament to the fusion of expertise, dedication, and a forward-looking vision. Its role in unraveling the complexities of resale pricing in the automotive domain establishes it as a noteworthy contribution to the realm of data science.

## Tech Stack

**Data Collection:** Google Open Source Data

**Data Analysis and Cleaning:** Pandas

**Machine Learning Models:** Scikit-learn

**Web Application Development:** Flask, Bootstrap

**Deployment:** Docker
## Screenshots

![App Screenshot 1](https://github.com/AnuraagaNath/Project-PredthePrice/blob/main/docker/static/img/Screenshot%20from%202023-12-23%2019-17-45.png?raw=true)

![App Screenshot 2](https://github.com/AnuraagaNath/Project-PredthePrice/blob/main/docker/static/img/Screenshot%20from%202023-12-23%2019-18-10.png?raw=true)


## Demo

![Demo Part 1](https://github.com/AnuraagaNath/Project-PredthePrice/assets/114306656/b3c8cd0c-be67-465c-b9f0-6c610b81f171)


![Demo Part 2](https://github.com/AnuraagaNath/Project-PredthePrice/assets/114306656/e9476e06-0e44-4ae4-922a-51b99f24841f)

## Run Locally

Run the project

```bash
  docker pull anuraaganath/pred-the-price:1.2.1
```
```bash
   docker container run -d -p 8000:5000 anuraaganath/pred-the-price:1.2.1
```
Check out the Docker Hub for updated versions of this project (if any)

https://hub.docker.com/r/anuraaganath/pred-the-price/tags



## License

[Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)


## Developer

- [@anuraaganath](https://www.github.com/anuraaganath)


## 🚀 About Me
I'm a Data Science Master's Student at BPPIMT, India.


## Feedback

If you have any feedback, please reach out to us at anuraaga.oct15@gmail.com

