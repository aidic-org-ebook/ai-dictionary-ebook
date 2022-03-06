# Activation Function
### Reference
https://deepai.org/machine-learning-glossary-and-terms/activation-function
### Status
Translated
### Definition
Hàm kích hoạt
### Description
Về bản chất, hàm kích hoạt thay đổi dữ liệu đầu ra cho neuron tiếp theo dựa vào tính chất của đầu vào.
Bằng việc thêm vào mạng sự 'phi tuyến tính', các hàm kích hoạt giúp mạng neuron hiểu được những hình mẫu phức tạp hơn.
Nếu không tồn tại những hàm này, mạng neuron bao nhiêu lớp cũng chỉ như một hàm tuyến tính cực lớn mà thôi.
### Figure
[{"path": "figures/A_Activation_Function.png", "caption": "Ví dụ về một hàm kích hoạt phổ biến: Rectified Linear Unit - ReLU", "width": 0.5}
### Tricks
Hàm kích hoạt được minh họa bên trên, ReLU, chỉ nên được dùng cho các hidden layers, vì nó có thể cho ra neuron 'chết' - neuron chỉ cho output = 0.

# Activation Level
### Reference
https://deepai.org/machine-learning-glossary-and-terms/activation-level
### Status
Translated
### Definition
Mức kích hoạt
### Description
Mức kích hoạt trong mạng nơ-ron nhân tạo là kết quả của hàm kích hoạt (Activation Function).
Kết quả này sau đó được sử dụng làm đầu vào cho nơ-ron kế tiếp.
### Figure
### Tricks

# Active Learning
### Reference
https://deepai.org/machine-learning-glossary-and-terms/active-learning
### Status
### Status
Translate
### Definition
Học tích cực
### Description
Học tích cực là một hình thức học bán giám sát (semi-supervised learning).
Cụm từ này diễn tả quá trình sắp xếp sự ưu tiên đối với những dữ liệu cần được gắn thẻ để có được kết quả tốt nhất trong việc huấn luyện một mô hình học có giám sát (supervised learning model).
Các bước học tích cực cô đọng:
1. Người sử dụng cần tự gắn nhãn một tệp dữ liệu mẫu nhỏ, sau đó huấn luyện mô hình trên tệp dữ liệu đó.
Mô hình này tuyệt nhiên sẽ không dùng được, nhưng nó giúp ta có cái nhìn tổng quát hơn về vùng nào cần được ưu tiên gắn nhãn hơn vùng khác.
2.  Sử dụng mô hình trên để phân loại những điểm dữ liệu (data point) còn lại, sau đó chấm điểm cho chúng.
Điểm này mang tên 'Điểm ưu tiên' (Priority score).
3. Lặp lại toàn quá trình trên: Một mô hình mới được huấn luyện dựa trên tệp dữ liệu đã được gắn thẻ của mô hình trước, sau đó sử dụng mô hình đó tiếp tục phân loại dữ  liệu chưa gắn thẻ để cập nhật quy cách gán điểm ưu tiên.
Bằng cách này, mô hình sẽ ngày càng chuẩn xác hơn.
### Figure
### Tricks
Trong thực tiễn, nếu một dự đoán của mô hình được người vận hành xác nhận là sai, dữ liệu đó có thể được sử dụng để tinh chỉnh (fine-tune) mô hình, hay nói cách khác, trở thành dữ liệu huấn luyện. Tuy nhiên, số lượng dữ liệu dùng để tinh chỉnh cần đạt một giá trị nhất định để có thể ảnh hưởng tới độ chính xác của mô hình.

# AdaBoost (Adaptive Boosting)
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Adadelta (Adaptive Delta)
### Reference
http://arxiv.org/abs/1212.5701
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Adam (Adaptive Momentum)
### Reference
https://arxiv.org/abs/1412.6980
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Adaptive Algorithm
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Adaptive Neuro Fuzzy Inference System (ANFIS)
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Adaptive Resonance Theory (ART)
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Adaptive Subgradient Methods
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Adversarial Learning
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Adversarial Machine Learning
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Affine Layer
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Affinity Analysis
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Affinity Matrix
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Affinity propagation clustering
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Agent Architecture
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Agent-based Model (ABM)
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Agglomerative clustering
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# AI Accelerator
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# AI-Complete problem
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Algorithm Analysis
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Algorithmic Learning Theory
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Algorithmic Probability
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Alpha and Beta cutoffs
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Alpha-Beta Pruning
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Ambient Intelligence (AmI)
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Analogical Reasoning
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Analogical Reasoning
### Reference
https://arxiv.org/pdf/1902.00120.pdf
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Analytic geometry
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Anchor Box
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Anomaly Detection
### Reference
https://deepai.org/machine-learning-glossary-and-terms/anomaly-detection
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Answer Literal
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Approximate Inference
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Approximate Training
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Approximation Algorithm
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Approximation Theory
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Area Under Curve - AUC
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# area under the PR curve
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Area under the ROC Curve
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Argument Extraction
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Argumentation Framework
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Artificial Bee Colony
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Artificial Consciousness
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Artificial Data Synthesis
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Artificial General Intelligence (AGI)
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Artificial Immune System (AIS)
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Artificial Intelligence (AI)
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Artificial Narrow Intelligence (ANI)
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Artificial Neural Networks - ANN
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Artificial Neurons
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Artificial Superintelligence (ASI)
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Artistic Style Transfer
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Association Learning
### Reference
https://deepai.org/machine-learning-glossary-and-terms/association-learning
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Association Rule Learning
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Associative Memory
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Attention Mechanism
### Reference
https://towardsdatascience.com/intuitive-understanding-of-attention-mechanism-in-deep-learning-6c9482aecf4f
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Attention Models
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Augmented Matrix
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Augmented Reality (AR)
### Reference
https://towardsdatascience.com/enhancing-ar-with-machine-learning-9214d2da75a6
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Augmented Transition Network - ATN
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Autoencoder
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Automated Planning And Scheduling
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Automated Reasoning
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Automatic Differentiation
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Automatic Interaction Detection
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Automatic Speech Recognition
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Automation Bias
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Autonomic Computing (AC)
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Autonomous Car
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Autonomous Robot
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Autonomous Supervised Learning
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Autonomous System
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Autonomous Vehicles
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Autoregessive Model
### Reference
https://deepai.org/machine-learning-glossary-and-terms/autoregressive-model
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Auxiliary Task Learning
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Average Pooling
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

# Avoidable Bias
### Reference
### Status
Pending
### Definition
### Description
### Figure
### Tricks

