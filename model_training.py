from datasets import load_dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments

def train_model():
    # Load dataset
    dataset = load_dataset("cnn_dailymail", "3.0.0")

    # Initialize model and tokenizer
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    tokenizer = T5Tokenizer.from_pretrained('t5-small')

    # Define training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
    )

    # Define trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset['train'],
        eval_dataset=dataset['validation']
    )

    # Train the model
    trainer.train()

    # Save the trained model
    model.save_pretrained("./trained_model")

    # Save the tokenizer
    tokenizer.save_pretrained("./trained_model")

# Run training
if __name__ == "__main__":
    train_model()
