import matplotlib.pyplot as plt
import pandas as pd

exp1 = 'experiments/baseline/gan1_base/gan1_base.csv'
exp2 = 'experiments/gan1_10_heads/gan1_10_heads.csv'
exp3 = 'experiments/gan1_10_heads_diff_data_for_heads/gan1_10_heads_diff_data_for_heads.csv'

df1 = pd.read_csv(exp1)
df2 = pd.read_csv(exp2)
df3 = pd.read_csv(exp3)
n = min(df1.shape[0], df2.shape[0], df3.shape[0])
df1 = df1.iloc[0:n, :]
df2 = df2.iloc[0:n, :]
df3 = df3.iloc[0:n, :]
epochs = [x * 2 for x in range(n)]

fig, axs = plt.subplots(2, 3, sharex=False, sharey=False, figsize=(12, 8))

axs[0, 0].plot(epochs, df1['fid_score'], 'k--', color='green', label='Baseline with 1 head')
axs[0, 0].plot(epochs, df2['fid_score'], 'k:', color='blue', label='10 heads')
axs[0, 0].plot(epochs, df3['fid_score'], label='10 heads + diff_data_for_heads', color='black')
axs[0, 0].set_xlabel('epoch', fontsize='x-large')
axs[0, 0].set_ylabel('FID', fontsize='large')

axs[0, 1].plot(epochs, df1['lossg_mean'], 'k--', color='green')
axs[0, 1].plot(epochs, df2['lossg_mean'], 'k:', color='blue')
axs[0, 1].plot(epochs, df3['lossg_mean'], color='black')
axs[0, 1].set_xlabel('epoch', fontsize='x-large')
axs[0, 1].set_ylabel(r'$V(G)$', fontsize='large')

axs[0, 2].plot(epochs, df1['lossd_mean'], 'k--', color='green')
axs[0, 2].plot(epochs, df2['lossd_mean'], 'k:', color='blue')
axs[0, 2].plot(epochs, df3['lossd_mean'], color='black')
axs[0, 2].set_xlabel('epoch', fontsize='x-large')
axs[0, 2].set_ylabel(r'$V(D)$', fontsize='large')

axs[1, 0].plot(epochs, df1['dgz_mean'] * -1, 'k--', color='green')
axs[1, 0].plot(epochs, df2['dgz_mean'] * -1, 'k:', color='blue')
axs[1, 0].plot(epochs, df3['dgz_mean'] * -1, color='black')
axs[1, 0].set_xlabel('epoch', fontsize='x-large')
axs[1, 0].set_ylabel(r'$-D(G(z))$', fontsize='large')

axs[1, 1].plot(epochs, df1['dx_mean'], 'k--', color='green')
axs[1, 1].plot(epochs, df2['dx_mean'], 'k:', color='blue')
axs[1, 1].plot(epochs, df3['dx_mean'], color='black')
axs[1, 1].set_xlabel('epoch', fontsize='x-large')
axs[1, 1].set_ylabel(r'$D(x)$', fontsize='large')

handles, labels = axs[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower right', fontsize='large')
plt.tight_layout()
plt.savefig('reports/gan1_baseline__gan1_10_heads__gan1_10_heads_diff_data_for_heads.pdf')
