import numpy as np
from matplotlib import pyplot as plt
from prettytable import PrettyTable


def plot_Results():
    for a in range(2):
        Eval =np.load('Evaluate_all.npy',allow_pickle=True)[a]

        Terms = ['WER','SER']
        for b in range(len(Terms)):
            learnper = [1, 2, 3, 4, 5]

            X = np.arange(5)
            plt.plot(learnper, Eval[:, 0,b], color='#aaff32', linewidth=3, marker='o', markerfacecolor='#aaff32', markersize=14,
                     label="RSO-HC-AARDNet")
            plt.plot(learnper, Eval[:, 1,b], color='#ad03de', linewidth=3, marker='o', markerfacecolor='#ad03de', markersize=14,
                     label="DMO-HC-AARDNet")
            plt.plot(learnper, Eval[:, 2,b], color='#8c564b', linewidth=3, marker='o', markerfacecolor='#8c564b', markersize=14,
                     label="BFGO-HC-AARDNet")
            plt.plot(learnper, Eval[:, 3,b], color='#ff000d', linewidth=3, marker='o', markerfacecolor='#ff000d', markersize=14,
                     label="HOA-HC-AARDNet")
            plt.plot(learnper, Eval[:, 4,b], color='k', linewidth=3, marker='o', markerfacecolor='k', markersize=14,
                     label="EHOA-HC-AARDNet")

            labels = ['1', '2', '3', '4', '5']
            plt.xticks(learnper, labels)

            plt.xlabel('KFOLD')
            plt.ylabel(Terms[b])
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
                       ncol=3, fancybox=True, shadow=True)
            path1 = "./Results/Dataset_%s_%s_line.png" % (a + 1, Terms[b])
            plt.savefig(path1)
            plt.show()

            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            X = np.arange(5)
            ax.bar(X + 0.00, Eval[:, 5,b], color='#aaff32', width=0.10, label="ResNet")
            ax.bar(X + 0.10, Eval[:, 6,b], color='#ad03de', width=0.10, label="CNN")
            ax.bar(X + 0.20, Eval[:, 7,b], color='#8c564b', width=0.10, label="DenseNet")
            ax.bar(X + 0.30, Eval[:, 8,b], color='#ff000d', width=0.10, label="ResDenseNet")
            ax.bar(X + 0.40, Eval[:, 9,b], color='k', width=0.10, label="EHOA-HC-AARDNet")
            # plt.xticks(X + 0.25, ('5', '10', '15', '20', '25'))


            labels = ['1', '2', '3', '4', '5']
            plt.xticks(X, labels)
            plt.xlabel('KFOLD')
            plt.ylabel(Terms[b])
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
                       ncol=3, fancybox=True, shadow=True)
            path1 = "./Results/Dataset_%s_%s_bar.png" % (a + 1, Terms[b])
            plt.savefig(path1)
            plt.show()


def optimize_plot_results():
    # matplotlib.use('TkAgg')
    eval = np.load('Eval_all.npy', allow_pickle=True)
    Terms = ['Accuracy', 'Sensitivity', 'Specificity', 'Precision', 'FPR', 'FNR', 'NPV', 'FDR', 'F1-Score', 'MCC']
    Graph_Term = [0, 1, 2, 3, 4,5,6, 7,8, 9]
    Algorithm = ['TERMS', 'RSO', 'DMO', 'BFGO', 'HOA', 'PROPOSED']
    Classifier = ['TERMS', 'ResNet', 'CNN', 'DenseNet', 'ResDenseNet', 'EHOA-HC-AARDNet']
    for i in range(eval.shape[0]):
        value = eval[i, 0, :, 4:]

        Table = PrettyTable()
        Table.add_column(Algorithm[0], Terms)
        for j in range(len(Algorithm) - 1):
            Table.add_column(Algorithm[j + 1], value[j, :])
        print('-------------------------------------------------- Dataset - ', i + 1, ' - Algorithm Comparison ',
              '--------------------------------------------------')
        print(Table)

        Table = PrettyTable()
        Table.add_column(Classifier[0], Terms)
        for j in range(len(Classifier) - 1):
            Table.add_column(Classifier[j + 1], value[len(Algorithm) + j - 1, :])
        print('-------------------------------------------------- Dataset - ', i + 1, ' - Classifier Comparison',
              '--------------------------------------------------')
        print(Table)

    learnper = [1, 2, 3, 4, 5]
    for i in range(eval.shape[0]):
        for j in range(len(Graph_Term)):
            Graph = np.zeros(eval.shape[1:3])
            for k in range(eval.shape[1]):
                for l in range(eval.shape[2]):
                    if j == 9:
                        Graph[k, l] = eval[i, k, l, Graph_Term[j] + 4]
                    else:
                        Graph[k, l] = eval[i, k, l, Graph_Term[j] + 4] * 100

            X = np.arange(5)
            plt.plot(learnper, Graph[:, 0], color='#aaff32', linewidth=3, marker='o', markerfacecolor='#aaff32',
                     markersize=14,
                     label="RSO-HC-AARDNet")
            plt.plot(learnper, Graph[:, 1], color='#ad03de', linewidth=3, marker='o', markerfacecolor='#ad03de',
                     markersize=14,
                     label="DMO-HC-AARDNet")
            plt.plot(learnper, Graph[:, 2], color='#8c564b', linewidth=3, marker='o', markerfacecolor='#8c564b',
                     markersize=14,
                     label="BFGO-HC-AARDNet")
            plt.plot(learnper, Graph[:, 3], color='#ff000d', linewidth=3, marker='o', markerfacecolor='#ff000d',
                     markersize=14,
                     label="HOA-HC-AARDNet")
            plt.plot(learnper, Graph[:, 4], color='k', linewidth=3, marker='o', markerfacecolor='k', markersize=14,
                     label="EHOA-HC-AARDNet")

            labels = ['1', '2', '3', '4', '5']
            plt.xticks(learnper, labels)

            plt.xlabel('KFOLD')
            plt.ylabel(Terms[Graph_Term[j]])
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
                       ncol=3, fancybox=True, shadow=True)
            path1 = "./Journ_Results/Dataset_%s_%s_line.png" % (i + 1, Terms[Graph_Term[j]])
            plt.savefig(path1)
            plt.show()

            fig = plt.figure()
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            X = np.arange(5)
            ax.bar(X + 0.00, Graph[:, 5], color='#aaff32', width=0.10, label="ResNet")
            ax.bar(X + 0.10, Graph[:, 6], color='#ad03de', width=0.10, label="CNN")
            ax.bar(X + 0.20, Graph[:, 7], color='#8c564b', width=0.10, label="DenseNet")
            ax.bar(X + 0.30, Graph[:, 8], color='#ff000d', width=0.10, label="ResDenseNet")
            ax.bar(X + 0.40, Graph[:, 9], color='k', width=0.10, label="EHOA-HC-AARDNet")
            # plt.xticks(X + 0.25, ('5', '10', '15', '20', '25'))

            labels = ['1', '2', '3', '4', '5']
            plt.xticks(X, labels)
            plt.xlabel('KFOLD')
            plt.ylabel(Terms[Graph_Term[j]])
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),
                       ncol=3, fancybox=True, shadow=True)
            path1 = "./Journ_Results/Dataset_%s_%s_bar.png" % (i + 1, Terms[Graph_Term[j]])
            plt.savefig(path1)
            plt.show()

optimize_plot_results()
# plot_Results()