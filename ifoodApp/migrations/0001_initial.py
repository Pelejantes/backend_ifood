# Generated by Django 3.2.5 on 2024-03-10 00:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuarioId', models.AutoField(primary_key=True, serialize=False)),
                ('nomeUsu', models.CharField(default=None, max_length=255, null=True)),
                ('telefoneUsu', models.CharField(default=None, max_length=14, null=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('emailUsu', models.EmailField(max_length=255, unique=True)),
                ('imagemPerfil', models.BinaryField(default=None, null=True)),
                ('statusAtivo', models.BooleanField(default=True)),
                ('dataCriacao', models.DateField(default=datetime.datetime.now)),
                ('codVerif', models.CharField(default=None, max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Acompanhamento',
            fields=[
                ('acompanhamentoId', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('qtdLimite', models.SmallIntegerField()),
                ('incluso', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AlternativasCampEsp',
            fields=[
                ('campoEspecificoId', models.AutoField(primary_key=True, serialize=False)),
                ('alternativa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('avaliacaoId', models.AutoField(primary_key=True, serialize=False)),
                ('qtdEstrelas', models.PositiveSmallIntegerField()),
                ('descricao', models.CharField(max_length=255)),
                ('dataAvaliacao', models.DateField()),
                ('usuarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CampoEspecifico',
            fields=[
                ('campoEspecificoId', models.AutoField(primary_key=True, serialize=False)),
                ('pergunta', models.CharField(max_length=255)),
                ('qtdLimite', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoriaId', models.AutoField(primary_key=True, serialize=False)),
                ('nomeCategoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ContaBancaria',
            fields=[
                ('contaBancariaId', models.AutoField(primary_key=True, serialize=False)),
                ('digitAgencia', models.CharField(max_length=2)),
                ('numConta', models.IntegerField()),
                ('nomeBanco', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Conversa',
            fields=[
                ('conversaId', models.AutoField(primary_key=True, serialize=False)),
                ('emissor', models.IntegerField()),
                ('receptor', models.IntegerField()),
                ('conteudo', models.TextField()),
                ('dataEnvio', models.DateField()),
                ('finalizada', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('cuponId', models.AutoField(primary_key=True, serialize=False)),
                ('valorDesconto', models.FloatField()),
                ('dataValidade', models.DateField()),
                ('limiteUso', models.SmallIntegerField()),
                ('valorMinimo', models.FloatField()),
                ('categoriaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('enderecoId', models.AutoField(primary_key=True, serialize=False)),
                ('logradouro', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=8)),
                ('bairro', models.CharField(default=None, max_length=255, null=True)),
                ('cidade', models.CharField(default=None, max_length=255, null=True)),
                ('estado', models.CharField(default=None, max_length=2, null=True)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('estabelecimentold', models.AutoField(primary_key=True, serialize=False)),
                ('nomeEstab', models.CharField(max_length=255)),
                ('telefoneEstab', models.CharField(max_length=14)),
                ('imagemEstab', models.BinaryField()),
                ('cnpj', models.CharField(max_length=14)),
                ('emailEstab', models.CharField(max_length=255)),
                ('codVerif', models.CharField(blank=True, max_length=6, null=True)),
                ('categoriaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.categoria')),
                ('enderecoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.endereco')),
            ],
        ),
        migrations.CreateModel(
            name='FormaPag',
            fields=[
                ('formaPag', models.AutoField(primary_key=True, serialize=False)),
                ('nomeFormaPag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('pedidoId', models.AutoField(primary_key=True, serialize=False)),
                ('statusPedido', models.CharField(max_length=50)),
                ('valorTotal', models.FloatField()),
                ('observacao', models.CharField(max_length=255)),
                ('dataPedido', models.DateField()),
                ('gorjeta', models.SmallIntegerField()),
                ('qtdItens', models.SmallIntegerField()),
                ('acompanhamentold', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.acompanhamento')),
                ('campoEspecificold', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.campoespecifico')),
                ('cuponld', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.cupon')),
                ('formaPagld', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.formapag')),
            ],
        ),
        migrations.CreateModel(
            name='PoliticaPrivacidade',
            fields=[
                ('politicaPrivacidadeId', models.AutoField(primary_key=True, serialize=False)),
                ('politica', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RegraCupon',
            fields=[
                ('regraCuponId', models.AutoField(primary_key=True, serialize=False)),
                ('descricaoRegra', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TermoUso',
            fields=[
                ('termoUsoId', models.AutoField(primary_key=True, serialize=False)),
                ('termo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('tipoUsuarioId', models.AutoField(primary_key=True, serialize=False)),
                ('nomeTipoUsuario', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoVeiculo',
            fields=[
                ('tipoVeiculoId', models.AutoField(primary_key=True, serialize=False)),
                ('nomeTipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SolicAtend',
            fields=[
                ('solicAtendId', models.AutoField(primary_key=True, serialize=False)),
                ('dataSolicitacao', models.DateField()),
                ('statusAtendimento', models.CharField(max_length=50)),
                ('conversaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.conversa')),
                ('pedidoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Seguranca',
            fields=[
                ('segurancaId', models.AutoField(primary_key=True, serialize=False)),
                ('dispConectados', models.SmallIntegerField()),
                ('usuarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('produtoId', models.AutoField(primary_key=True, serialize=False)),
                ('nomeProd', models.CharField(max_length=255)),
                ('disponibilidade', models.BooleanField()),
                ('preco', models.FloatField()),
                ('imagemProd', models.BinaryField()),
                ('alcoolico', models.BooleanField()),
                ('descricao', models.CharField(max_length=255)),
                ('avaliacaoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.avaliacao')),
                ('categoriaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.categoria')),
                ('estabelecimentoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.estabelecimento')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='produtold',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.produto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuariold',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('notificacaoId', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=255)),
                ('dataRecebimento', models.DateField()),
                ('cuponId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.cupon')),
            ],
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('favoritosId', models.AutoField(primary_key=True, serialize=False)),
                ('estabelecimentoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.estabelecimento')),
                ('usuarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EntregadorVeic',
            fields=[
                ('tipoVeiculoId', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=8)),
                ('cnh', models.CharField(max_length=11)),
                ('usuarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoEntrega',
            fields=[
                ('enderecoEntregaId', models.AutoField(primary_key=True, serialize=False)),
                ('enderecoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.endereco')),
                ('usuarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cupon',
            name='regraCuponId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.regracupon'),
        ),
        migrations.CreateModel(
            name='ConfigNotif',
            fields=[
                ('configNotifId', models.AutoField(primary_key=True, serialize=False)),
                ('permNotificacao', models.BooleanField()),
                ('permNotifEmail', models.BooleanField()),
                ('permNotifWhatsapp', models.BooleanField()),
                ('permNotifSms', models.BooleanField()),
                ('usuarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('cartaold', models.AutoField(primary_key=True, serialize=False)),
                ('nomeBandeira', models.CharField(max_length=255)),
                ('numCartao', models.CharField(max_length=16)),
                ('validade', models.DateField()),
                ('cvv', models.CharField(max_length=3)),
                ('nomeTitular', models.CharField(max_length=255)),
                ('cpfCnpj', models.CharField(max_length=14)),
                ('apelidoCartao', models.CharField(max_length=255)),
                ('usuarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='contaBancariaId',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.contabancaria'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipoUsuarioId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ifoodApp.tipousuario'),
        ),
    ]
