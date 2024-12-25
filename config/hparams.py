class Hparams:
    class Audio:
            # 梅尔频谱参数
            num_mels = 80  # 梅尔频谱的维度，通常在80到128之间
            min_mel_freq = 30.  # 梅尔频谱的最低频率，单位为Hz
            max_mel_freq = 7600.  # 梅尔频谱的最高频率，单位为Hz
    
            # PPG和瓶颈特征参数
            ppg_dim = 351  # PPG特征的维度
            bn_dim = 256  # 瓶颈特征的维度
    
            # STFT参数
            num_freq = 1025  # STFT频率维度，通常为FFT点数的一半加一
    
            # 采样率和帧参数
            sample_rate = 16000  # 采样率，单位为Hz，常见值为16000或22050
            frame_length_ms = 25  # 帧长，单位为毫秒，通常为20到40毫秒
            frame_shift_ms = 10  # 帧移，单位为毫秒，通常为帧长的一半
    
            # 基频参数
            upper_f0 = 500.  # 基频的最高值，单位为Hz
            lower_f0 = 30.  # 基频的最低值，单位为Hz
    
            # MFCC参数
            n_mfcc = 13  # MFCC特征的维度，通常为13
    
            # 预加重参数
            preemphasize = 0.97  # 预加重系数，通常在0.95到0.97之间
    
            # 归一化参数
            min_level_db = -80.0  # 最低dB值，用于归一化
            ref_level_db = 20.0  # 参考dB值，用于归一化
            max_abs_value = 1.  # 归一化后的最大绝对值
            symmetric_specs = False  # 是否对称归一化
    
            # Griffin-Lim算法参数
            griffin_lim_iters = 60  # Griffin-Lim算法的迭代次数
            power = 1.5  # 幅度谱的幂次
    
            # 窗函数处理参数
            center = True  # 是否在每帧中心进行窗函数处理

    class SPEAKERS:
        num_spk = 3  # 说话人数
        spk_to_inds = ['bzn', 'mst-female', 'mst-male']  # 说话人标识符列表

    class TrainToOne:
        dev_set_rate = 0.1  # 验证集比例
        test_set_rate = 0.05  # 测试集比例
        epochs = 60  # 训练轮数
        train_batch_size = 32  # 训练批次大小
        test_batch_size = 1  # 测试批次大小
        shuffle_buffer = 128  # 数据打乱缓冲区大小
        shuffle = True  # 是否打乱数据
        learning_rate = 1e-3  # 学习率
        num_workers = 16  # 数据加载的工作线程数

    class TrainToMany:
        dev_set_rate = 0.1  # 验证集比例
        test_set_rate = 0.05  # 测试集比例
        epochs = 60  # 训练轮数
        train_batch_size = 32  # 训练批次大小
        test_batch_size = 1  # 测试批次大小
        shuffle_buffer = 128  # 数据打乱缓冲区大小
        shuffle = True  # 是否打乱数据
        learning_rate = 1e-3  # 学习率
        num_workers = 16  # 数据加载的工作线程数

    class BLSTMConversionModel:
        lstm_hidden = 256  # LSTM隐藏层维度

    class BLSTMToManyConversionModel:
        lstm_hidden = 256  # LSTM隐藏层维度
        spk_embd_dim = 64  # 说话人嵌入维度

    class ResidualNet:
        other_params = {
            'param1': 'value1',
            'param2': 'value2'
            # 添加其他需要的参数
        }
