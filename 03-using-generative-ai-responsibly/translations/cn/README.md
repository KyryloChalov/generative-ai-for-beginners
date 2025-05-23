# 第三章 ： 负责任地使用生成式人工智能

[![Using Generative AI Responsibly](../../images/03-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson3-gh?WT.mc_id=academic-105485-koreyst)

人们很容易对人工智能尤其是生成式人工智能着迷，但你需要考虑如何负责任地使用它。 你需要考虑如何确保输出是公平的、无害的等等。 本章旨在为您提供上述相关背景信息、需要考虑的事项以及如何采取积极措施来改善人工智能的使用。

## 本章概述

本章内容包括：

- 为什么在构建生成式人工智能应用程序时应优先考虑负责任的人工智能。
- 负责任的人工智能的核心原则以及它们与生成式人工智能的关系。
- 如何通过策略和工具将这些负责任的人工智能原则付诸实践。

## 学习目标

学完本章内容后您将了解到：

- 构建生成式人工智能应用程序时负责任的人工智能的重要性。
- 在构建生成式 AI 应用程序时何时思考和应用 Responsible AI 的核心原则。
- 您可以使用哪些工具和策略来将 Responsible AI 的概念付诸实践。

## 负责任的人工智能原则

生成式人工智能的热度非常高。 这种热度为这个领域带来了许多新的开发人员、关注和资金。 虽然这对于任何想要使用生成式人工智能构建产品和公司的人来说都是非常积极的，但我们负责任地行事也很重要。

在整个课程中，我们专注于构建“Our startup”和相关人工智能教育产品。 我们将使用负责任的人工智能的原则：公平、包容、可靠性/安全、安全和隐私、透明度和问责制。 根据这些原则，我们将探讨它们与我们在产品中使用生成式人工智能的关系。

## 为什么你应该优先考虑负责任的人工智能

在构建产品时，采取以人为本的方法并牢记用户的最大利益会带来最大的爱意

生成式人工智能的独特性在于它能够为用户创建有用的答案、信息、指导和内容。 无需许多手动步骤即可完成此操作，这可以带来非常令人印象深刻的结果。 不幸的是如果没有适当的规划和策略，它也可能会给您的用户、产品和整个社会带来一些有害的结果。

让我们看看这些潜在有害结果中的一些（但不是全部）：

### 幻觉

幻觉是一个术语，用于描述 LLMs 产生的内容要么完全无意义，要么根据给出其他错误的信息。

举个例子，我们为“Our startup”构建了一个功能，允许学生向模型提出历史问题。 一名学生问“泰坦尼克号的唯一幸存者是谁？”

该模型产生如下响应：

![提示说“谁是泰坦尼克号的唯一幸存者”](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp?WT.mc_id=academic-105485-koreyst)

> _（来源：[飞翔的野牛](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

给出了一个非常确切的答案。 不幸的是，这是不正确的。 即使极少了解，人们也会发现泰坦尼克号幸存者不止一名。 但对于刚开始研究这个领域的学生来说，这个答案足以有说服力，不会被质疑并被视为事实。 这样做的后果可能会导致人工智能系统不可靠，并对我们初创公司的声誉产生负面影响。

在任何给定的 LLMs 的每次迭代中，我们都看到了在最大限度地减少幻觉方面的性能改进。 即使有了这样的改进，我们作为应用程序构建者和用户仍然需要意识到这些限制。

### 有害内容

我们在前面的部分中介绍了 LLMs 会产生不正确或毫无意义的回答。 我们需要注意的另一个风险是模型产生有害内容。

有害内容可以定义为：

- 提供指示或鼓励自残或伤害某些群体。
- 仇恨或侮辱性内容。
- 指导策划任何类型的攻击或暴力行为。
- 提供有关如何查找非法内容或实施非法行为的说明。
- 展示露骨的色情内容。

对于我们的初创公司来说，我们希望确保拥有正确的工具和策略来防止学生看到此类内容。

### 缺乏公平性

公平的定义是“确保人工智能系统没有偏见和歧视，并公平、平等地对待每个人。” 在生成式人工智能的世界中，我们希望确保模型的输出不会强化边缘群体的排他性世界观。

这些类型的输出不仅会破坏为用户建立积极的产品体验，还会造成进一步对社会进行危害。 作为应用程序构建者，在使用生成式人工智能构建解决方案时，我们应该始终牢记广泛且多样化的用户群。

## 如何负责任地使用生成式人工智能

现在我们已经确定了负责任的生成式人工智能的重要性，让我们看看我们可以采取的 4 个步骤来负责任地构建我们的人工智能解决方案：

![缓解循环](../../images/mitigate-cycle.png?WT.mc_id=academic-105485-koreyst)

### 衡量潜在危害

在软件测试中，我们测试用户对应用程序的预期操作。 同样，测试用户最有可能使用的一组不同的提示是衡量潜在危害的好方法。

由于“Our startup”正在开发教育产品，因此最好准备一份与教育相关的提示列表。 这可以涉及某个主题、历史事实和有关学生生活的提示。

### 减轻潜在危害

现在是时候寻找方法来预防或限制模型及其响应造成的潜在危害了。 我们可以从 4 个不同的层面来看待这个问题：

![缓解层](../../images/mitigation-layers.png?WT.mc_id=academic-105485-koreyst)

- **模型**。 为正确的用例选择正确的模型。 当应用于更小、更具体的用例时，更大、更复杂的模型（例如 GPT-4）可能会导致更大的有害内容风险。 使用训练数据进行微调还可以降低有害内容的风险。

- **安全系统**。 安全系统是平台上为模型服务的一组工具和配置，有助于减轻伤害。 Azure OpenAI Service 上的内容过滤系统就是一个例子。 系统还应该检测越狱攻击和不需要的活动，例如来自网络机器人的请求。

- **元提示**。 元提示和基础是我们可以根据某些行为和信息指导或限制模型的方法。 这可以使用系统输入来定义模型的某些限制。 此外，提供与系统范围或领域更相关的输出。

  它还可以使用检索增强生成 (RAG) 等技术，让模型仅从选定的可信来源中提取信息。 本课程后面有一章关于[构建搜索应用程序](../../../08-building-search-applications/translations/cn/README.md?WT.mc_id=academic-105485-koreyst)的内容

- **用户体验**。 最后一层是用户通过应用程序界面以某种方式直接与模型交互的地方。 通过这种方式，我们可以设计 UI/UX 来限制用户可以发送到模型的输入类型以及向用户显示的文本或图像。 在部署人工智能应用程序时，我们还必须透明地了解我们的生成式人工智能应用程序可以做什么和不能做什么。

我们有一章内容致力于[为人工智能应用程序设计用户体验](../../../12-designing-ux-for-ai-applications/translations/cn/README.md?WT.mc_id=academic-105485-koreyst)

- **评估模型**。 与 LLMs 合作可能具有挑战性，因为我们并不总是能够控制模型训练的数据。 无论如何，我们应该始终评估模型的性能和输出。 衡量模型的准确性、相似性、基础性和输出的相关性仍然很重要。 这有助于为应用相关人员和用户提供透明度和信任。

### 运营负责任的生成式人工智能解决方案

围绕人工智能应用程序构建操作实践是最后阶段。 这包括与“Our startup”的其他部门（例如法律和安全部门）合作，以确保我们遵守所有监管政策。 在发布之前，我们还希望围绕交付、处理事件和回滚制定计划，以防止扩大对用户造成的任何伤害。

## 相关工具

虽然开发负责任 AI 解决方案的工作量可能看起来很多，但这是值得付出的。 随着生成式人工智能领域的发展，更多帮助开发人员有效地将责任整合到工作流程中的工具将会更成熟。 如，[Azure AI 内容安全](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) 可以通过 API 请求帮助检测有害内容和图像。

## 知识检查

为了确保负责任地使用人工智能，您需要注意哪些事项？

1. 答案正确。
2. 有害使用，即人工智能不用于犯罪目的。
3. 确保人工智能不存在偏见和歧视。

答：2 和 3 是正确的。 负责任的人工智能可以帮助您考虑如何减轻有害影响和偏见等。

## 🚀 知识拓展

阅读 [Azure AI 内容安全](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) 并了解您可以采用什么方法。

## 继续学习

想要了解更多有关如何负责任地使用生成式 AI 进行构建的信息？ 转至[进阶学习的页面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 查找有关本章的其他重要资源。

前往第四章，我们将了解 [提示工程基础](../../../04-prompt-engineering-fundamentals/translations/cn/README.md?WT.mc_id=academic-105485-koreyst)！
