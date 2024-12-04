import datasets


def process_docs(dataset: datasets.Dataset):
    def _process_doc(doc):

        question = doc["question"]
        subject = doc["subject"]
        formatted_choices = "\n".join(f"{chr(65 + i)}. {choice}" for i, choice in enumerate(doc["choices"]))

        rendered_text = doc["template"].format(
            subject=doc["subject"], question=doc["question"], choices=formatted_choices
        )
        # print("render", rendered_text)

        return {
            "template": rendered_text,
            "subject": subject,
            "question": question,
            "choices": formatted_choices,
        }

    return dataset.map(_process_doc)
