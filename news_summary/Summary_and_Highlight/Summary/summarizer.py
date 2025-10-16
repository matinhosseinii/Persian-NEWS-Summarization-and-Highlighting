from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def load_model(local_model_path):
  
  # Load the tokenizer and model from the local directory
  tokenizer = AutoTokenizer.from_pretrained(local_model_path, use_fast=False)
  model = AutoModelForSeq2SeqLM.from_pretrained(local_model_path)
  return tokenizer, model



def get_summary(path, text):

  tokenizer, model = load_model(path)

  inputs = tokenizer(text, return_tensors="pt") # .to(device)

  # Generate summary
  summary_ids = model.generate(inputs['input_ids'], max_length=150, num_beams=4, length_penalty=2.0, early_stopping=True)

  # Decode the summary
  summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

  return summary



def get_summaries(text):
  summaries = {}
  summaries['p_b2b'] = get_summary('Summary_and_Highlight\Summary\HooshvareLab pn-summary-b2b-shared', text)
  summaries['p_mt5'] = get_summary('Summary_and_Highlight\Summary\HooshvareLab pn-summary-mt5-small', text)
  summaries['f_b2b'] = get_summary('Summary_and_Highlight\Summary\matinhosseini finetuned-b2b-with-xlsum', text)
  summaries['f_mt5'] = get_summary('Summary_and_Highlight\Summary\matinhosseini finetuned-mt5small-with-xlsum', text)

  for model in summaries.keys():
    while '[ZWNJ]' in summaries[model]:
      summaries[model] = summaries[model].replace(' [ZWNJ] ', '&zwnj;')

  return summaries


# text = """محمدرضا جان‌نثاری، رئیس ستاد انتخابات استان اصفهان ۱۵ تیر در نشست ستاد انتخابات که با حضور رؤسا و اعضای کمیته‌های ستاد انتخابات استان برگزار شد، ضمن تسلیت ایام محرم الاحرام اظهار کرد: هئیت‌های نظارت و اجرایی و تمام دستگاه‌های مرتبط آماده برگزاری رأی‌گیری بوده و همزمان با کل کشور فرآیند آغاز شد. این فرآیند بدون هیچ مشکلی شروع شد، دستگاه‌های احراز هویت تست‌گیری شده و امیدوارم این انتخابات باشکوه باشد.

# وی افزود: از مردم می‌خواهیم در ساعات اولیه حضور یابند و سعی کنند در همین ساعات رای خود را بیندازند. مرحله نخست از ساعت ۸ تا ۱۸ است، اما بنا به سوابق تمدید خواهد شد، ولی مردم سعی کنند از حقشان استفاده کرده و در همان ابتدای روز حضور یابند.

# جان‌نثاری تصریح کرد: در ساختار مردم‌سالاری این نظام، حق مردم در این امر به طور کامل در نظر گرفته شده است. یاد می‌کنیم از شهدای خدمت و شهید رئیسی و امیدوارم به برکت خون آن‌ها انتخابات باشکوهی داشته و مردم دنبال باشند که نظام اسلامی با قوت ادامه دهد.

# رئیس ستاد انتخابات استان اصفهان تاکید کرد: این انتخابات و شکوه آن یکی از راه‌های پاسداشت خون شهدای خدمت است و این انتخابات است که سبب قوت نظام می‌شوند. مردم نیز پای صندوق رای خواهند بود و همچون ۴۵ سال گذشته پای کار خواهند بود.

# او در پایان افزود: مردم مجری انتخابات و رسانه‌ها انعکاس دهنده این انتخاب مردمی هستند.

# انتهای پیام"""
# print(get_summaries(text))