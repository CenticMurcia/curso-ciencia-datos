<h1 align="center">Preparación de los datos</h1>


## Definir el problema: Clasificación o Regresión




## Selección del conjunto de validación




## Preprocesamiento

<table>
  <tr>
    <tD></tD>
    <tD>
      <h4>Tree based models</h4>
      <ul>
        <li>Decission Tree</li>
        <li>Random Forest</li>
        <li>Extra Trees</li>
        <li>Adaboost</li>
        <li>Gradient Boosting</li>
        <li>XGBoost</li>
        <li>LightGBM</li>
        <li>CatBoost</li>
      </ul>
    </tD>
    <td>
      <h4>No-tree based models</h4>
      <ul>
        <li>Linear Models</li>
        <li>Neural Networks</li>
        <li>K-Nearest Neighbors</li>
        <li>Suport Vector Machines</li>
      </ul>
    </td>
  </tr>
  <tr>
    <th>Categorical<br>Ordinal</th>
    <td>
      <ul>
        <li><b>Ordinal encoding</b></li>
        <li>Other: Frequency encoding</li>
      </ul>
    </td>
    <td>
      <ul>
        <li><b>One hot encoding</b></li>
        <li>Other: Embedding</li>
      </ul>
    </td>
  </tr>
  <tr>
    <th>Numerical</th>
    <td><b>Nothing</b></td>
    <td>
      <ul>
        <li>MinMaxScaler</li>
        <li><b>StandarScaler</b></li>
        <li>Skewed?
          <ul>
            <li>np.log(1+x)</li>
            <li>np.sqrt(x+2/3)</li>
            <li>Box-Cox</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>




## Categorical features

| Ordinal Encoding o Label Encoding    | One-Hot Encoding        | Target Encoding o Mean Encoding |
|--------------------------------------|-------------------------|---------------------------------|
| ![](img/enc-ord.png)                 | ![](img/enc-onehot.png) | ![](img/enc-target.png)         |


## Models

| Model                 | Comment                              | Library                    | More info |
|:---------------------:|--------------------------------------|----------------------------|-----------|
| **Decission Tree**    | Simple and explicable.               | Sklearn                    |           |
| **Linear models**     | Simple and explicable.               | Sklearn                    |           |
| **Random Forest**     | Good starting point (tree enesemble) | Sklearn                    |           |
| **Gradient Boosting** | Usually the best (tree enesemble)    | XGBoost, LighGBM, Catboost |           |
| **Neural Network**    | Good if lot of data.                 | Fast.ai v2                 | [blog](https://hackernoon.com/gain-state-of-the-art-results-on-tabular-data-with-deep-learning-and-embedding-layers-a-how-to-guide-r17b36k8) |

