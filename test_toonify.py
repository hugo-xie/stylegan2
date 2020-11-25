import pretrained_networks

if __name__ == '__main__':

    blended_path = "/home/xieyu/project/stylegan2_pretrain_ckpt/ffhq-cartoon-blended-64.pkl"
    ffhq_path = "/home/xieyu/project/stylegan2_pretrain_ckpt/stylegan2-ffhq-config-f.pkl"

    _,_, Gs_blended = pretrained_networks.load_networks(blended_path)
    _,_, Gs         = pretrained_networks.load_networks(ffhq_path)


