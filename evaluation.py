from datasets import load_metric # type: ignore

def compute_rouge(pred, tokenizer):
    rouge = load_metric('rouge')
    labels_ids = pred.label_ids
    pred_ids = pred.predictions.argmax(-1)
    pred_str = tokenizer.batch_decode(pred_ids, skip_special_tokens=True)
    labels_str = tokenizer.batch_decode(labels_ids, skip_special_tokens=True)
    
    rouge_output = rouge.compute(predictions=pred_str, references=labels_str)
    return {
        "rouge1": rouge_output["rouge1"].mid.fmeasure,
        "rouge2": rouge_output["rouge2"].mid.fmeasure,
        "rougeL": rouge_output["rougeL"].mid.fmeasure,
    }
