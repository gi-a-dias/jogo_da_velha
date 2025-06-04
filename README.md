
# Flutter WebView App

Este é um projeto Flutter simples que utiliza o plugin `webview_flutter` para exibir uma aplicação web dentro de um aplicativo Android. Ele foi preparado para ser assinado e empacotado para produção (`release`).

## 📱 Funcionalidade

- Abre uma WebView apontando para um servidor local ou remoto.
- Usa permissões adequadas para acesso à internet.
- Compatível com Android SDK 35 e NDK 27.
- Já configurado para assinatura com chave `.jks`.

## 🚀 Como rodar

1. **Instale as dependências**:

   ```bash
   flutter pub get
   ```

2. **Execute no dispositivo físico**:

   ```bash
   flutter run
   ```

3. **Compile para release (com assinatura)**:

   ```bash
   flutter build apk --release
   ```

## 🔐 Assinatura (release)

Certifique-se de ter um arquivo `key.properties` com o seguinte conteúdo:

```properties
storeFile=android/app/my-key.jks
storePassword=******
keyAlias=minha-chave
keyPassword=******
```

E a chave `.jks` deve estar no caminho correto (`android/app/my-key.jks`).

## 📁 Estrutura do Projeto

```
flutter_webview_release/
├── android/
│   ├── app/
│   │   ├── build.gradle
│   │   ├── my-key.jks
│   │   └── key.properties
│   └── build.gradle
├── lib/
│   └── main.dart
├── pubspec.yaml
└── README.md
```

## 🧪 Dependências

```yaml
dependencies:
  flutter:
    sdk: flutter
  webview_flutter: ^4.2.2
```

## 🌐 Permissões

Certifique-se de que o `AndroidManifest.xml` tem a permissão:

```xml
<uses-permission android:name="android.permission.INTERNET"/>
```

## 🛠 Requisitos

- Flutter 3.32+
- Android SDK 35
- Android NDK 27.0.12077973
- Java 11+

## 👩‍💻 Desenvolvido por

Giovanna Dias — Projeto de integração com sistema web via WebView.
