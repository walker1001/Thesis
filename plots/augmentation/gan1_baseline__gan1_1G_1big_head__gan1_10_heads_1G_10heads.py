import matplotlib.pyplot as plt
import pandas as pd

exp1 = 'experiments/augmentation/gan1_baseline/gan1_baseline.csv'
exp2 = 'experiments/augmentation/gan1_10_heads_1G_10heads/gan1_10_heads_1G_10heads.csv'
exp3 = 'experiments/augmentation/gan1_10_heads_1G_10heads_diff_data_for_heads/gan1_10_heads_1G_10heads_diff_data_for_heads.csv'
exp4 = 'experiments/augmentation/gan1_1G_1big_head/gan1_1G_1big_head.csv'

df1 = pd.read_csv(exp1)
df2 = pd.read_csv(exp2)
df3 = pd.read_csv(exp3)
df4 = pd.read_csv(exp4)
n = min(df1.shape[0], df2.shape[0], df3.shape[0], df4.shape[0], 100)
df1 = df1.iloc[0:n, :]
df2 = df2.iloc[0:n, :]
df3 = df3.iloc[0:n, :]
df4 = df4.iloc[0:n, :]
epochs = [x * 8 for x in range(n)]

fig, axs = plt.subplots(2, 3, sharex=False, sharey=False, figsize=(12, 8))

n1 = 10
n2 = n
df1_ = df1.iloc[n1:n2, :]
df2_ = df2.iloc[n1:n2, :]
df3_ = df3.iloc[n1:n2, :]
df4_ = df4.iloc[n1:n2, :]
epochs_ = epochs[n1:n2]
axs[0, 0].plot(epochs_, df1_['fid_score'], 'k--', color='green', label='Baseline')
axs[0, 0].plot(epochs_, df2_['fid_score'], 'k:', color='blue', label='10 heads')
axs[0, 0].plot(epochs_, df3_['fid_score'], label='10 heads + diff_data', color='black')
axs[0, 0].plot(epochs_, df4_['fid_score'], label='Baseline + big head', color='orange')
axs[0, 0].set_xlabel('epoch', fontsize='x-large')
axs[0, 0].set_ylabel('FID', fontsize='large')

axs[0, 1].plot(epochs, df1['fid_score'], 'k--', color='green')
axs[0, 1].plot(epochs, df2['fid_score'], 'k:', color='blue')
axs[0, 1].plot(epochs, df3['fid_score'], color='black')
axs[0, 1].plot(epochs, df4['fid_score'], color='orange')
axs[0, 1].set_xlabel('epoch', fontsize='x-large')
axs[0, 1].set_ylabel('FID', fontsize='large')

axs[0, 2].plot(epochs, df1['lossd_mean'], 'k--', color='green')
axs[0, 2].plot(epochs, df2['lossd_mean'], 'k:', color='blue')
axs[0, 2].plot(epochs, df3['lossd_mean'], color='black')
axs[0, 2].plot(epochs, df4['lossd_mean'], color='orange')
axs[0, 2].set_xlabel('epoch', fontsize='x-large')
axs[0, 2].set_ylabel(r'$V(D)$', fontsize='large')

axs[1, 0].plot(epochs, df1['dgz_mean'] * -1, 'k--', color='green')
axs[1, 0].plot(epochs, df2['dgz_mean'] * -1, 'k:', color='blue')
axs[1, 0].plot(epochs, df3['dgz_mean'] * -1, color='black')
axs[1, 0].plot(epochs, df4['dgz_mean'] * -1, color='orange')
axs[1, 0].set_xlabel('epoch', fontsize='x-large')
axs[1, 0].set_ylabel(r'$-D(G(z))$', fontsize='large')

axs[1, 1].plot(epochs, df1['dx_mean'], 'k--', color='green')
axs[1, 1].plot(epochs, df2['dx_mean'], 'k:', color='blue')
axs[1, 1].plot(epochs, df3['dx_mean'], color='black')
axs[1, 1].plot(epochs, df4['dx_mean'], color='orange')
axs[1, 1].set_xlabel('epoch', fontsize='x-large')
axs[1, 1].set_ylabel(r'$D(x)$', fontsize='large')

axs[1, 2].plot(epochs, df1['lossg_mean'], 'k--', color='green')
axs[1, 2].plot(epochs, df2['lossg_mean'], 'k:', color='blue')
axs[1, 2].plot(epochs, df3['lossg_mean'], color='black')
axs[1, 2].plot(epochs, df4['lossg_mean'], color='orange')
axs[1, 2].set_xlabel('epoch', fontsize='x-large')
axs[1, 2].set_ylabel(r'$V(G)$', fontsize='large')

# handles, labels = axs[0, 0].get_legend_handles_labels()
# fig.legend(handles, labels, loc='lower right', fontsize='large')
# plt.tight_layout()

handles, labels = axs[0, 0].get_legend_handles_labels()
axs[1, 1].legend(handles=handles, labels=labels, loc='lower center',
                 bbox_to_anchor=(0.45, -0.5), fancybox=False, shadow=False,
                 ncol=4, fontsize='xx-large')
plt.subplots_adjust(bottom=0.2, wspace=0.32, top=0.95, left=0.07, right=0.98, hspace=0.25)


# plt.subplots_adjust(top=.9, bottom=0.3, right=0.99, left=0.05,
#                     hspace=0, wspace=0.32)
plt.savefig('reports/augmentation/gan1_baseline__gan1_1G_1big_head__gan1_10_heads_1G_10heads.pdf')