import torch

Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

MSE = torch.nn.MSELoss()


class RFLoss():
    @staticmethod
    def compute_lossd(discriminator, gen_imgs, real_imgs):
        real_labels = Tensor(real_imgs.shape[0]).fill_(1.0)
        gen_labels = Tensor(gen_imgs.shape[0]).fill_(0.0)

        real_preds = discriminator(real_imgs, -1)
        real_loss = MSE(real_preds, real_labels)

        gen_preds = discriminator(gen_imgs, -1)
        gen_loss = MSE(gen_preds, gen_labels)

        return real_loss + gen_loss
    
    @staticmethod
    def compute_lossg(discriminator, gen_imgs):
        real_labels = Tensor(gen_imgs.shape[0]).fill_(1.0)
        lossg = MSE(discriminator(gen_imgs, -1), real_labels)
        return lossg
