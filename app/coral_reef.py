import coral_reef

# Install and set up the Coral platform with PyTorch support
coral_reef.install(pytorch=True)

# Test the Edge TPU Accelerator
coral_reef.test()

# Run a sample PyTorch script using the Edge TPU Accelerator
coral_reef.run_sample('pytorch_classification.py', ['--model', 'models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.pth',
                                                    '--labels', 'models/inat_bird_labels.txt',
                                                    '--input', 'images/parrot.jpg',
                                                    '--output', 'results/parrot.jpg',
                                                    '--top_k', '3'])
