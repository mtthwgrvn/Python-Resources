text = "X-DSPAM-Confidence:    0.8475";
spam = text.find('.')
end = text.find('5')
host = float(text[spam:end+1])

print(host)
