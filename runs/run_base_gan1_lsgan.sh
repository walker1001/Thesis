python -m src.train --exp_name 'gan1_base' \
                    --loss_name 'gan1' \
                    --augmentation '0' \
                    --spec_g '0' \
                    --spec_d '1' \
                    --dist 'gauss' \
                    --n_epochs '200' \
                    --n_heads '1' \
                    --interval '2'

python -m src.train --exp_name 'lsgan_base' \
                    --loss_name 'lsgan' \
                    --augmentation '0' \
                    --spec_g '0' \
                    --spec_d '1' \
                    --dist 'gauss' \
                    --n_epochs '200' \
                    --n_heads '1' \
                    --interval '2'
