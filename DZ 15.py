y = {}
x = ('By November 1932, the Nazi Party had the most seats in the German Reichstag but did not have a majority. As a result, no party was able to form a majority parliamentary coalition in support of a candidate for chancellor. Former chancellor Franz von Papen and other conservative leaders persuaded President Paul von Hindenburg to appoint Hitler as chancellor on 30 January 1933. Shortly after, the Reichstag passed the Enabling Act of 1933 which began the process of transforming the Weimar Republic into Nazi Germany, a one-party dictatorship based on the totalitarian and autocratic ideology of Nazism. Hitler aimed to eliminate Jews from Germany and establish a New Order to counter what he saw as the injustice of the post-World War I international order dominated by Britain and France. His first six years in power resulted in rapid economic recovery from the Great Depression, the abrogation of restrictions imposed on Germany after World War I, and the annexation of territories inhabited by millions of ethnic Germans, which gave him significant popular support.').lower()
for i in x.split():
    y[i] = y.get(i, 0) + 1
    print(i, y[i])
# Я не понимаю как сделать так чтобы слова не повторялись и записался только конечный результат.
# буду благодарен за подсказку ибо самому додумыватся уже времени нет:(


