# Persian NEWS Summarization and Highlighting
### 🧠 Models Used

| Purpose | Model | Hugging Face Link | Description |
|----------|--------|------------------|--------------|
| Base Model 1 | `HooshvareLab/pn-summary-b2b-shared` | [🔗 Link](https://huggingface.co/HooshvareLab/pn-summary-b2b-shared) | A b2b-shared model on the pnSummary dataset to summarize articles. |
| Base Model 2 | `HooshvareLab/pn-summary-mt5-base` | [🔗 Link](https://huggingface.co/HooshvareLab/pn-summary-mt5-base) | An mT5-base model on the pnSummary dataset to summarize articles. |
| Fine-tuned Model 1 | `matinhosseini/finetuned-b2b-with-xlsum` | [🔗 Link](https://huggingface.co/matinhosseini/finetuned-b2b-with-xlsum) | Fine-tuned `b2b-shared` on Persian news dataset (XLsum) for text summarization. |
| Fine-tuned Model 2 | `matinhosseini/finetuned-mt5small-with-xlsum` | [🔗 Link](https://huggingface.co/matinhosseini/finetuned-mt5small-with-xlsum) | Fine-tuned `mt5-small` on Persian news dataset (XLsum) for text summarization. |

---

### ⚙️ Tech Stack

- **Backend:** Django  
- **Frontend:** Bootstrap  
- **Web Scraping:** Selenium & BeautifulSoup  
- **Core NLP:** some algorithms for highlighting + fine-tuned LLMs for summarization  

---

### 🙌 Personal Note
This was my **first complete project**, built during my **Bachelor’s thesis**.  
It may not be perfectly structured or fully optimized, but it represents my early steps into applied NLP and model fine-tuning.
